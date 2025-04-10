const fs = require('fs');
const path = require('path');

// 경로 설정
const algorithmRoot = path.join(__dirname, 'public', 'data', 'algorithm');
const outputPath = path.join(algorithmRoot, 'index.json');

// 🔁 모든 하위 폴더 중 description.md 또는 code.py가 있는 폴더만 수집
function getAllFoldersRecursively(dir, platform = '') {
  const result = [];

  function recurse(currentPath, relativePath) {
    const entries = fs.readdirSync(currentPath, { withFileTypes: true });
    let hasValidFile = false;

    entries.forEach((entry) => {
      const fullPath = path.join(currentPath, entry.name);
      if (entry.isDirectory()) {
        recurse(fullPath, path.join(relativePath, entry.name));
      } else if (entry.isFile() && (entry.name === 'description.md' || entry.name === 'code.py')) {
        hasValidFile = true;
      }
    });

    if (hasValidFile) {
      result.push({ folderPath: currentPath, relativePath });
    }
  }

  recurse(dir, platform); // 시작할 때 platform 자체가 상대 경로가 됨
  return result;
}

// 📌 문자열을 제목으로 변환 (하이픈, 밑줄 → 공백, 각 단어 대문자)
function formatTitleFromSlug(slug) {
  return slug
    .replace(/[-_]/g, ' ')
    .replace(/\b\w/g, (c) => c.toUpperCase());
}

// ✅ 알고리즘 인덱스 생성 함수
async function generateIndex() {
  const platforms = fs.readdirSync(algorithmRoot).filter((file) =>
    fs.statSync(path.join(algorithmRoot, file)).isDirectory()
  );

  const allFolders = [];

  // 각 플랫폼별 폴더 순회
  platforms.forEach((platform) => {
    const fullPath = path.join(algorithmRoot, platform);
    const folders = getAllFoldersRecursively(fullPath, platform);
    allFolders.push(...folders);
  });

  const indexData = [];

  for (const { folderPath, relativePath } of allFolders) {
    const slugParts = relativePath.split(path.sep);
    const slug = slugParts.join('/'); // 플랫폼/폴더명 형태
    const title = formatTitleFromSlug(slugParts[slugParts.length - 1]);
    const descriptionPath = path.join(folderPath, 'description.md');
    let description = '';

    if (fs.existsSync(descriptionPath)) {
      description = fs.readFileSync(descriptionPath, 'utf-8').split('\n')[0];
    } else {
      description = '문제 설명이 없습니다.';
    }

    indexData.push({
      id: slug, // ex: leetcode/two-sum 또는 boj/1000
      title,
      description,
      tags: [],
      thumbnail: `/data/algorithm/${slug}/thumbnail.png`,
    });
  }

  fs.writeFileSync(outputPath, JSON.stringify(indexData, null, 2), 'utf-8');
  console.log('✅ index.json 생성 완료');
}

// 실행
generateIndex();
