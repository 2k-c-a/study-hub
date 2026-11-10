// 모임 만들기 폼과 모임 상세 (detail.html)
const params = new URLSearchParams(location.search);
const area = document.getElementById('study-detail');

function renderCreateForm() {
  const form = document.createElement('form');
  form.innerHTML = `
    <h1>모임 만들기</h1>
    <div class="form-field"><label for="title">모임 이름</label><input id="title" name="title"></div>
    <div class="form-field"><label for="description">소개</label><textarea id="description" name="description" rows="3"></textarea></div>
    <div class="form-field"><label for="place">장소</label><input id="place" name="place"></div>
    <div class="form-field"><label for="max_members">최대 인원</label><input id="max_members" name="max_members" type="number" value="4" min="2" max="20"></div>
    <p class="message" id="form-message"></p>
    <button class="btn btn-primary" type="submit">만들기</button>
  `;
  form.addEventListener('submit', async (event) => {
    event.preventDefault();
    const body = {
      title: form.title.value,
      description: form.description.value,
      place: form.place.value,
      max_members: form.max_members.value,
    };
    try {
      const { id } = await request('/api/studies', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body),
      });
      location.href = `detail.html?id=${id}`;
    } catch (error) {
      document.getElementById('form-message').textContent = error.message;
    }
  });
  area.replaceChildren(form);
}

function line(tag, className, text) {
  const node = document.createElement(tag);
  if (className) node.className = className;
  node.textContent = text;
  return node;
}

async function renderDetail(id) {
  const study = await request(`/api/studies/${id}`);
  document.title = `${study.title} · study-hub`;
  const edit = line('button', 'btn', '모임 수정');
  edit.type = 'button';
  edit.addEventListener('click', () => {
    // TODO: 모임 수정 (PUT /api/studies/<id>)
  });
  area.replaceChildren(
    line('h1', '', study.title),
    line('p', '', study.description || '소개가 아직 없습니다.'),
    line('p', 'meta', `장소: ${study.place || '미정'} · 최대 ${study.max_members}명`),
    line('p', 'meta', `만든 날: ${study.created_at}`),
    edit,
  );
}

if (params.has('new')) renderCreateForm();
else if (params.get('id')) renderDetail(params.get('id'));
