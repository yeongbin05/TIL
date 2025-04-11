const fs = require('fs');
const path = require('path');

const algorithmRoot = path.join(__dirname, 'public', 'data', 'algorithm');
const outputPath = path.join(algorithmRoot, 'index.json');

function getAllFoldersRecursively(dir, platform = '') {
  const result = [];

  function recurse(currentPath, relativePath) {
    const entries = fs.readdirSync(currentPath, { withFileTypes: true });
    let hasValidFile = false;

    entries.forEach((entry) => {
      const fullPath = path.join(currentPath, entry.name);
      if (entry.isDirectory()) {
        recurse(fullPath, path.join(relativePath, entry.name));
      } else if (
        entry.isFile() &&
        (entry.name === 'description.md' || entry.name === 'code.py')
      ) {
        hasValidFile = true;
      }
    });

    if (hasValidFile) {
      result.push({ folderPath: currentPath, relativePath });
    }
  }

  recurse(dir, platform);
  return result;
}

function formatTitleFromSlug(slug) {
  return slug
    .replace(/[-_]/g, ' ')
    .replace(/\b\w/g, (c) => c.toUpperCase());
}

// 🔍 description과 tags 파싱 (tags는 항상 첫 줄)
function parseMarkdown(mdContent) {
  const lines = mdContent.split(/\r?\n/); // cross-platform
  let tags = [];
  let description = '';

  // 1. tags 줄 찾기
  const tagLine = lines.find(line => line.trim().startsWith('tags:'));
  if (tagLine) {
    const match = tagLine.match(/\[(.*?)\]/);
    if (match && match[1]) {
      tags = match[1].split(',').map((tag) => tag.trim());
    }
  }

  // 2. 첫 줄이 tags면 그 다음 비어있지 않은 줄부터 description
  const tagLineIndex = lines.findIndex(line => line.trim().startsWith('tags:'));
  for (let i = tagLineIndex + 1; i < lines.length; i++) {
    if (lines[i].trim() !== '') {
      description = lines[i].trim();
      break;
    }
  }

  // fallback
  if (!description) {
    description = lines.find((line) => line.trim() !== '') || '문제 설명이 없습니다.';
  }

  return { description, tags };
}


async function generateIndex() {
  const platforms = fs.readdirSync(algorithmRoot).filter((file) =>
    fs.statSync(path.join(algorithmRoot, file)).isDirectory()
  );

  const allFolders = [];

  platforms.forEach((platform) => {
    const fullPath = path.join(algorithmRoot, platform);
    const folders = getAllFoldersRecursively(fullPath, platform);
    allFolders.push(...folders);
  });

  const indexData = [];

  for (const { folderPath, relativePath } of allFolders) {
    const slugParts = relativePath.split(path.sep);
    const slug = slugParts.join('/');
    const title = formatTitleFromSlug(slugParts[slugParts.length - 1]);

    const descriptionPath = path.join(folderPath, 'description.md');
    let description = '문제 설명이 없습니다.';
    let tags = [];

    if (fs.existsSync(descriptionPath)) {
      const content = fs.readFileSync(descriptionPath, 'utf-8');
      const parsed = parseMarkdown(content);
      description = parsed.description;
      tags = parsed.tags;
    }

    indexData.push({
      id: slug,
      title,
      description,
      tags,
      thumbnail: `/data/algorithm/${slug}/thumbnail.png`,
    });
  }

  fs.writeFileSync(outputPath, JSON.stringify(indexData, null, 2), 'utf-8');
  console.log('✅ index.json 생성 완료');
}

generateIndex();
