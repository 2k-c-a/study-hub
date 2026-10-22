# study-hub API

서버는 Flask(`app.py`), 데이터는 sqlite3(`db.py`, `schema.sql`)입니다. 모든 응답은 JSON입니다.
오류는 `{"error": "메시지"}` 형식으로, 상태 코드와 함께 돌려줍니다.

## 모임

| 메서드 | 경로 | 설명 |
| --- | --- | --- |
| GET | `/api/studies` | 모임 목록 |
| POST | `/api/studies` | 모임 만들기 |
| GET | `/api/studies/<id>` | 모임 상세 |
| DELETE | `/api/studies/<id>` | 모임 삭제 |

모임 하나는 다음 모양입니다.

```json
{
  "id": 1,
  "title": "알고리즘 스터디",
  "description": "매주 문제 3개씩 풀고 리뷰합니다.",
  "place": "도서관 3층 세미나실",
  "max_members": 6,
  "created_at": "2026-10-22 10:00:00"
}
```

`POST /api/studies` 본문은 `title`, `description`, `place`, `max_members`이고, 만들어지면 `201`과 `{"id": 새 id}`를 돌려줍니다.

## 회원

| 메서드 | 경로 | 설명 |
| --- | --- | --- |
| POST | `/api/signup` | 회원가입 (`username`, `password`) |
| POST | `/api/login` | 로그인 (`username`, `password`) |

로그인에 성공하면 `{"ok": true, "username": "..."}`를 돌려줍니다. 비밀번호는 해시로 저장합니다.

## 앞으로 할 일

- 모임 수정 (`PUT /api/studies/<id>`)
- 모임 이름 검색 (`GET /api/studies?q=`)
