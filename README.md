# 🎸 Tone Lab 실행 방법

## 폴더 구조
```
tone-lab/
├─ index.html   ← 사이트 본체 (소리 합성, 이펙터, 파형)
├─ server.py    ← 내 컴퓨터에서 사이트를 띄우는 서버
└─ README.md
```

## 실행하기
1. 폴더를 바탕화면 등에 저장해요.
2. 터미널(윈도우: 명령 프롬프트 또는 PowerShell)을 열고 폴더로 이동해요.
   `cd 폴더경로`
3. 서버를 실행해요.
   - 윈도우: `python server.py`
   - 맥: `python3 server.py`
4. 브라우저가 자동으로 열려요. 안 열리면 주소창에 `http://localhost:8000` 입력!
5. 끌 때는 터미널에서 `Ctrl + C`.

## 왜 서버가 필요할까?
브라우저는 보안 때문에 **마이크/오디오 입력을 `localhost` 또는 `https` 주소에서만** 허용해요.
index.html을 더블클릭해서 여는 방식(file://)은 실제 기타 입력이 막힐 수 있어요.

## 문제 해결
- `python`을 찾을 수 없다고 나오면 → 파이썬 설치 확인 (python.org), 맥은 `python3` 사용
- 포트가 사용 중이라고 나오면 → `python server.py 8080` 처럼 번호를 바꿔요
- 기타 소리가 안 들리면 → 브라우저 마이크 권한 허용 + 입력 장치(오디오 인터페이스) 선택
- 하울링(삑 소리) → 반드시 이어폰·헤드폰 사용

## 인터넷에 공개하려면 (https 자동 제공)
- **Netlify Drop**: app.netlify.com/drop 에 폴더를 끌어다 놓기 (server.py는 필요 없어요)
- **GitHub Pages**: 저장소에 index.html 올리고 Pages 켜기

## 다음에 추가해 볼 기능
1. 프리셋 저장/불러오기  2. 튜너  3. 이펙터 순서 바꾸기  4. 입력 녹음 후 파일 저장  5. 코드 선택(C, D, Em…)
