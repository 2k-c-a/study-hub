// 서버 API 호출 모음 (docs/api.md)

// 서버가 오류를 돌려주면 화면 위쪽에 메시지를 띄운다(빈 화면 대신).
function showError(message) {
  let box = document.getElementById('error-banner');
  if (!box) {
    box = document.createElement('p');
    box.id = 'error-banner';
    box.className = 'message';
    box.setAttribute('role', 'alert');
    document.querySelector('main')?.prepend(box);
  }
  box.textContent = message;
}

async function request(url, options = {}) {
  let res;
  try {
    res = await fetch(url, options);
  } catch {
    showError('서버에 연결하지 못했습니다. 서버가 켜져 있는지 확인하세요.');
    throw new Error('network');
  }
  if (res.status === 204) return null;
  const data = await res.json().catch(() => null);
  if (!res.ok) {
    const message = data?.error || `서버 오류가 발생했습니다 (${res.status}).`;
    showError(message);
    throw new Error(message);
  }
  return data;
}

const api = {
  listStudies: () => request('/api/studies'),
  deleteStudy: (id) => request(`/api/studies/${id}`, { method: 'DELETE' }),
};
