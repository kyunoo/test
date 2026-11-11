"""
Tone Lab 로컬 서버 (파이썬 기본 기능만 사용, 설치할 것 없음)

실행 방법:  python server.py      (맥/리눅스는 python3 server.py)
종료 방법:  터미널에서 Ctrl + C
"""
import http.server      # 웹 서버를 만들어 주는 파이썬 기본 도구
import socketserver     # 접속을 받아서 처리해 주는 도구
import webbrowser       # 브라우저를 자동으로 열어 주는 도구
import os
import sys

PORT = 8000  # 주소 끝에 붙는 번호. 이미 쓰는 중이면 python server.py 8080 처럼 바꿔서 실행

# 이 파일(server.py)이 있는 폴더를 웹사이트의 "홈"으로 삼아요.
os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Handler(http.server.SimpleHTTPRequestHandler):
    """index.html 같은 파일을 브라우저에 전달하는 담당자"""

    def end_headers(self):
        # 파일을 고칠 때마다 새로고침으로 바로 확인할 수 있게 캐시를 끕니다.
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *args):
        # 누가 어떤 파일을 요청했는지 터미널에 한 줄로 보여 줘요.
        print("요청:", self.path)


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else PORT
    socketserver.TCPServer.allow_reuse_address = True

    # "127.0.0.1" = 내 컴퓨터에서만 접속 가능 (같은 와이파이의 다른 사람은 못 들어와요)
    with socketserver.TCPServer(("127.0.0.1", port), Handler) as server:
        url = f"http://localhost:{port}"
        print("=" * 44)
        print(" Tone Lab 서버가 켜졌어요!")
        print(f" 주소: {url}")
        print(" 끄려면 Ctrl + C 를 누르세요")
        print("=" * 44)
        webbrowser.open(url)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\n서버를 종료했어요.")


if __name__ == "__main__":
    main()
