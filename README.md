# FastAPI 프로젝트

FastAPI를 사용한 간단한 REST API 서버입니다.

## 요구사항

- Python 3.8 이상

## 설치 방법

### 1. 가상환경 생성 (권장)

```bash
python -m venv venv
```

### 2. 가상환경 활성화

**macOS/Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

### 3. 의존성 설치

```bash
pip install -r requirements.txt
```

## 실행 방법

### 개발 서버 실행

```bash
uvicorn main:app --reload
```

- `main`: `main.py` 파일
- `app`: FastAPI 인스턴스 이름
- `--reload`: 코드 변경 시 자동 재시작 (개발 모드)

### 호스트 및 포트 지정

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## API 문서

서버 실행 후 아래 URL에서 자동 생성된 API 문서를 확인할 수 있습니다:

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## API 엔드포인트

| 메서드 | 경로 | 설명 |
|--------|------|------|
| GET | `/` | Hello World 반환 |
| GET | `/items/{item_id}` | 아이템 조회 (쿼리 파라미터 `q` 지원) |

### 예시

```bash
# 루트 엔드포인트
curl http://127.0.0.1:8000/

# 아이템 조회
curl http://127.0.0.1:8000/items/1?q=test
```

