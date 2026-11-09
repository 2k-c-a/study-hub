// 모임 목록 (index.html)
function el(tag, className, text) {
  const node = document.createElement(tag);
  if (className) node.className = className;
  if (text !== undefined) node.textContent = text;
  return node;
}

function studyCard(study) {
  const li = el('li', 'card');
  const title = el('h3');
  const link = el('a', '', study.title);
  link.href = `detail.html?id=${study.id}`;
  title.append(link);
  const desc = el('p', '', study.description || '');
  const meta = el('p', 'meta', `${study.place || '장소 미정'} · 최대 ${study.max_members}명`);
  const remove = el('button', 'btn btn-danger', '삭제');
  remove.type = 'button';
  remove.addEventListener('click', async () => {
    if (!confirm(`'${study.title}' 모임을 삭제할까요?`)) return;
    await api.deleteStudy(study.id);
  });
  li.append(title, desc, meta, remove);
  return li;
}

async function renderStudies() {
  const list = document.getElementById('study-list');
  const studies = await api.listStudies();
  list.replaceChildren(...studies.map(studyCard));
  if (!studies.length) list.append(el('li', 'empty', '아직 모임이 없습니다. 첫 모임을 만들어 보세요.'));
}

renderStudies();
