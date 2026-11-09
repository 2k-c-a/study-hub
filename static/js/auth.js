// 로그인 · 회원가입 폼 (login.html, signup.html)
async function postJson(url, body) {
  const res = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });
  const data = await res.json().catch(() => ({}));
  return { ok: res.ok, data };
}

function bindAuthForm(formId, url, onSuccess) {
  const form = document.getElementById(formId);
  if (!form) return;
  const message = document.getElementById('auth-message');
  form.addEventListener('submit', async (event) => {
    event.preventDefault();
    message.textContent = '';
    const body = {
      username: form.username.value.trim(),
      password: form.password.value,
    };
    const { ok, data } = await postJson(url, body);
    if (!ok) {
      message.textContent = '요청을 처리하지 못했습니다.';
      return;
    }
    onSuccess(data);
  });
}

bindAuthForm('login-form', '/api/login', (data) => {
  localStorage.setItem('studyhub.user', data.username);
  location.href = 'index.html';
});

bindAuthForm('signup-form', '/api/signup', () => {
  alert('가입되었습니다. 로그인해 주세요.');
  location.href = 'login.html';
});
