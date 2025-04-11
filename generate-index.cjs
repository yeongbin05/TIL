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

// ✅ tags, date, description 파싱
// 🔧 기존 parseMarkdown 함수에서 설명 추출 개선
function parseMarkdown(mdContent) {
  const lines = mdContent.split(/\r?\n/);
  let tags = [];
  let date = null;
  let description = '';

  for (let line of lines) {
    const trimmed = line.trim();
    if (trimmed.startsWith('tags:')) {
      const match = trimmed.match(/\[(.*?)\]/);
      if (match && match[1]) {
        tags = match[1].split(',').map((tag) => tag.trim());
      }
    } else if (trimmed.startsWith('date:')) {
      date = trimmed.replace('date:', '').trim();
    } else if (
      description === '' &&
      !trimmed.startsWith('tags:') &&
      !trimmed.startsWith('date:') &&
      trimmed !== ''
    ) {
      // ⚠️ date, tags 제외한 첫 설명 줄
      description = trimmed;
    }
  }

  return { description, tags, date };
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
    let date = null;

    if (fs.existsSync(descriptionPath)) {
      const content = fs.readFileSync(descriptionPath, 'utf-8');
      const parsed = parseMarkdown(content);
      description = parsed.description;
      tags = parsed.tags;
      date = parsed.date || new Date().toISOString().slice(0, 10); // 없으면 오늘 날짜
    }

    indexData.push({
      id: slug,
      title,
      description,
      tags,
      date,
      thumbnail: `/data/algorithm/${slug}/thumbnail.png`,
    });
  }

  // ✅ 최신순 정렬
  indexData.sort((a, b) => new Date(b.date) - new Date(a.date));

  fs.writeFileSync(outputPath, JSON.stringify(indexData, null, 2), 'utf-8');
  console.log('✅ index.json 생성 완료');
}

generateIndex();
