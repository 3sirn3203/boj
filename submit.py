import os
from pathlib import Path
from dotenv import load_dotenv
from seleniumbase import SB


def login_if_needed(sb: SB, timeout: int = 15) -> None:
    load_dotenv()
    username = os.getenv("ID")
    password = os.getenv("PASSWORD")
    if not username or not password:
        raise RuntimeError("Missing ID / PASSWORD in .env")

    # 로그인 링크 클릭
    sb.wait_for_element('a[href^="/login"]', timeout=timeout)
    sb.click('a[href^="/login"]')

    # 로그인 폼 입력 후 제출(Enter)
    sb.wait_for_element('input[name="login_user_id"]', timeout=timeout)
    sb.type('input[name="login_user_id"]', username)

    sb.wait_for_element('input[name="login_password"]', timeout=timeout)
    sb.type('input[name="login_password"]', password + "\n")  # Enter로 submit


def submit_solution(url: str, problem_num: int, src_path: str, headless: bool = True, timeout: int = 15) -> None:

    with SB(uc=True, test=False, headless=headless) as sb:

        sb.uc_open_with_reconnect(url, reconnect_time=1)
        sb.uc_gui_handle_captcha()

        # 0) 로그인
        login_if_needed(sb, timeout=timeout)

        # 1) 문제 페이지에서 제출 링크 클릭
        sb.wait_for_element(f'a[href="/submit/{problem_num}"]', timeout=timeout)
        sb.click(f'a[href="/submit/{problem_num}"]')

        # 2) CodeMirror 로딩 대기 후 코드 주입
        src_file = Path(src_path)
        if not src_file.exists():
            raise FileNotFoundError(f"Source file not found: {src_path}")
        code = src_file.read_text(encoding="utf-8")

        sb.wait_for_element(".CodeMirror", timeout=timeout)
        sb.execute_script(
            "document.querySelector('.CodeMirror').CodeMirror.setValue(arguments[0]);",
            code
        )

        # 3) 제출 버튼 클릭
        sb.wait_for_element("#submit_button", timeout=timeout)
        sb.click("#submit_button")

        # 제출 후 상태 페이지로 넘어가는지 대기(환경에 따라 URL 패턴은 달라질 수 있음)
        sb.wait_for_ready_state_complete()
        sb.wait_for_element('table#status-table', timeout=timeout)