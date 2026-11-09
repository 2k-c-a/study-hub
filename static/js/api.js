// 서버 API 호출 모음 (docs/api.md)
const api = {
  async listStudies() {
    const res = await fetch('/api/studies');
    return res.json();
  },
  async deleteStudy(id) {
    const res = await fetch(`/api/studies/${id}`, { method: 'DELETE' });
    if (!res.ok) throw new Error('모임을 삭제하지 못했습니다.');
  },
};
