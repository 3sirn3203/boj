import sys
import subprocess
import requests
from pathlib import Path
from typing import List
from argparse import ArgumentParser
from bs4 import BeautifulSoup

from submit import submit_solution

URL = "https://www.acmicpc.net/problem/"
SRC_DIR = "src/"
TEST_DIR = "test/"

def normalize_ws(s: str) -> str:
    return " ".join(s.split())

def extract_sample_test_cases(html: str):
    soup = BeautifulSoup(html, "lxml")

    in_pres = soup.select('pre[id^="sample-input-"]')
    out_pres = soup.select('pre[id^="sample-output-"]')

    sample_input = [pre.get_text() for pre in in_pres]
    sample_output = [normalize_ws(pre.get_text()) for pre in out_pres]

    return sample_input, sample_output

def load_sample_test_cases_via_browser(url: str, timeout: int = 15, headless: bool = True):
    from seleniumbase import SB

    with SB(uc=True, test=False, headless=headless) as sb:
        sb.uc_open_with_reconnect(url, reconnect_time=1)
        sb.uc_gui_handle_captcha()
        sb.wait_for_element("#problem_description", timeout=timeout)
        html = sb.get_page_source()

    return extract_sample_test_cases(html)

def load_sample_test_cases(url: str, timeout: int = 10, headless: bool = True):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
    }

    try:
        resp = requests.get(url, headers=headers, timeout=timeout)
        if resp.status_code == 202 or resp.headers.get("x-amzn-waf-action") == "challenge":
            raise RuntimeError("Blocked by AWS WAF challenge")
        resp.raise_for_status()
        if not resp.text.strip():
            raise RuntimeError("Empty response body")

        sample_input, sample_output = extract_sample_test_cases(resp.text)
        if not sample_input and not sample_output:
            raise RuntimeError("Sample test cases not found in response")

        return sample_input, sample_output
    except Exception as exc:
        print(f"Direct fetch failed ({exc}); trying browser fetch...")
        return load_sample_test_cases_via_browser(url, timeout=timeout, headless=headless)

def load_user_test_cases(test_path: str):
    text = Path(test_path).read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")
    lines = text.split("\n")

    user_input = []
    user_output = []
    state = None  # None | "input" | "output"
    cur_in = []
    cur_out = []

    def flush_case():
        nonlocal cur_in, cur_out
        inp = "\n".join(cur_in).strip()
        out = "\n".join(cur_out).strip()
        if inp or out:
            # input/output 둘 다 있을 때만 케이스로 인정
            if inp and out:
                user_input.append(inp)
                user_output.append(out)
        cur_in = []
        cur_out = []

    for raw in lines:
        line = raw.strip()

        if line.lower() == "input":
            if cur_in or cur_out:
                flush_case()
            state = "input"
            continue

        if line.lower() == "output":
            state = "output"
            continue

        if state == "input":
            if line == "" and not cur_in:
                continue
            cur_in.append(raw.rstrip("\n"))
        elif state == "output":
            if line == "" and not cur_out:
                continue
            cur_out.append(raw.rstrip("\n"))
        else:
            continue

    if cur_in or cur_out:
        flush_case()

    return user_input, user_output

def run_script_with_input(script_path: str, input_str: str, timeout: int = 5):
    proc = subprocess.run(
        [sys.executable, script_path],
        input=(input_str + "\n"),
        text=True,
        capture_output=True,
        timeout=timeout,
    )

    # 런타임 에러(Exit code != 0)면 stderr 포함해서 예외로 올림
    if proc.returncode != 0:
        raise RuntimeError(
            f"Script exited with code {proc.returncode}\n"
            f"[stderr]\n{proc.stderr.strip()}\n"
            f"[stdout]\n{proc.stdout.strip()}"
        )

    return proc.stdout

def check_special_judge(script_path: str, input_list: List[str], output_list: List[str], 
                    timeout: int = 5, type: str = "Sample"):
    results = []

    for i in range(len(input_list)):
        inp = input_list[i]
        expected = output_list[i]

        try:
            raw_out = run_script_with_input(script_path, inp, timeout=timeout)
            got = normalize_ws(raw_out)
            results.append((i + 1, inp, expected, got, None))
        except Exception as e:
            results.append((i + 1, inp, expected, "", str(e)))

    print(f"{type} Test Cases Results ({len(input_list)} test cases):")
    for case_no, inp, expected, got, err in results:
        print(f"  [Case {case_no}]")
        print("    Expected:", normalize_ws(expected))
        print("    Got     :", got)
    print()

def check_test_case(script_path: str, input_list: List[str], output_list: List[str], 
                    timeout: int = 5, type: str = "Sample"):
    results = []
    all_pass = True

    for i in range(len(input_list)):
        inp = input_list[i]
        expected = normalize_ws(output_list[i])

        try:
            raw_out = run_script_with_input(script_path, inp, timeout=timeout)
            got = normalize_ws(raw_out)

            ok = (got == expected)
            all_pass = all_pass and ok

            results.append((i + 1, ok, inp, expected, raw_out, None))
        except Exception as e:
            all_pass = False
            results.append((i + 1, False, inp, expected, "", str(e)))

    print(f"{type} Test Cases Results ({len(input_list)} test cases):")
    for case_no, ok, inp, expected, got, err in results:
        status = "PASS" if ok else "FAIL"
        print(f"  [Case {case_no}] {status}")
        if err:
            print("Error:", err)
        else:
            if not ok:
                print("    Expected:", expected)
                print("    Got     :")
                print("===== Log =====")
                print(got, end='')
                print("===============")
    print()

    return all_pass


def main():
    parser = ArgumentParser()
    parser.add_argument("--num_prob", type=int, default=1000, help="Problem number")
    parser.add_argument("--timeout", type=int, default=5, help="Timeout in seconds for each test case")
    parser.add_argument("--submit", action="store_true", help="Automatically submit if all tests pass")
    parser.add_argument("--headless", type=bool, default=True, help="Run browser in headless mode")
    parser.add_argument("--special-judge", action="store_true", help="Use special judge")
    args = parser.parse_args()

    url = f"{URL}{args.num_prob}"
    src_path = f"{SRC_DIR}{args.num_prob}.py"
    test_path = f"{TEST_DIR}{args.num_prob}.txt"

    sample_input, sample_output = load_sample_test_cases(url, headless=args.headless)

    if not Path(src_path).exists():
        raise FileNotFoundError(f"Source file not found: {src_path}")
    
    user_input, user_output = [], []
    if Path(test_path).exists():
        user_input, user_output = load_user_test_cases(test_path)

    assert len(sample_input) == len(sample_output), "Mismatched number of sample inputs and outputs"
    assert len(user_input) == len(user_output), "Mismatched number of user-created inputs and outputs"
    
    if args.special_judge:
        check_special_judge(src_path, sample_input, sample_output, timeout=args.timeout, type="Sample")
        if user_input:
            check_special_judge(src_path, user_input, user_output, timeout=args.timeout, type="User")
        if args.submit:
            print("\nSubmitting solution...")
            submit_solution(url, args.num_prob, src_path, headless=args.headless, timeout=15)
            print("Solution submitted.")
            
    else:
        pass_provided = check_test_case(src_path, sample_input, sample_output, timeout=args.timeout, type="Sample")
        pass_user = check_test_case(src_path, user_input, user_output, timeout=args.timeout, type="User") if user_input else True

        if pass_provided and pass_user:
            print("All test cases passed!")
            if args.submit:
                print("\nSubmitting solution...")
                submit_solution(url, args.num_prob, src_path, headless=args.headless, timeout=15)
                print("Solution submitted.")
        else:
            print("Error in some test cases.")


if __name__ == "__main__":
    main()
