// 모임 이름 검색 (index.html): 이미 그려진 카드를 이름으로 거른다.
const searchInput = document.getElementById('study-search');

function applySearch() {
  const keyword = searchInput.value.trim().toLowerCase();
  for (const card of document.querySelectorAll('#study-list .card')) {
    const title = card.querySelector('h3')?.textContent.toLowerCase() || '';
    card.hidden = keyword !== '' && !title.includes(keyword);
  }
}

searchInput.addEventListener('input', applySearch);
