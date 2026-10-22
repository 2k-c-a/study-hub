# study-hub

스터디 모임을 만들고 찾는 작은 웹 사이트입니다. 3인 팀 프로젝트입니다.

> **주의:** 이 저장소는 GitViz 시연 영상용 교육 저장소로, 보안 취약점(SQL 주입)이 들어간 코드를 **일부러** 포함합니다.
> 서버는 `127.0.0.1`에서만 실행하고 인터넷에 공개하지 마세요. 실제 서비스에 이 코드를 쓰지 마세요.

## 기술

- 백엔드: Python 3, Flask, sqlite3
- 화면: 빌드 없는 HTML · CSS · JavaScript (`static/`)
- 테스트: pytest

## 실행

```bash
python -m venv .venv
.venv\Scripts\activate          # macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python app.py                   # http://127.0.0.1:5000
```

테스트: `pytest`

## 폴더 구조

```text
study-hub/
├─ app.py            Flask 라우트
├─ db.py             DB 접근
├─ schema.sql        테이블 정의
├─ static/           화면 (HTML · CSS · JS)
├─ tests/            pytest 테스트
└─ docs/api.md       API 문서
```

## 역할

| 사람 | 맡는 일 |
| --- | --- |
| 우혁 (팀장) | 페이지 구조 · 목록 · 문서 |
| 지석 | 화면 디자인 · 로그인 화면 |
| 도영 | 서버 · DB · 테스트 |

## 협업 규칙

- `main`에서 브랜치를 만들어 작업하고 PR로 올립니다.
- 리뷰어의 Approve를 받은 뒤 병합합니다(Create a merge commit).
- 커밋 메시지는 `feat:`, `fix:`, `chore:`, `docs:`로 시작합니다.
