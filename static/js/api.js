// 서버 API 호출 모음 (docs/api.md)
const api = {
  async listStudies() {
    const res = await fetch('/api/studies');
    return res.json();
  },
  async deleteStudy(id) {
    await fetch(`/api/studies/${id}`, { method: 'DELETE' });
  },
};
