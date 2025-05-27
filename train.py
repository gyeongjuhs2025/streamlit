import tkinter as tk
from tkinter import ttk, messagebox
import threading
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

CONFIG_FILE = "config.json"

# ---------------- Selenium 자동화 함수 ----------------
def run_automation(center, username, password, status_label):
    try:
        update_status(status_label, "브라우저 준비 중...")

        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

        update_status(status_label, "로그인 페이지 접속 중...")
        driver.get("https://www.neti.go.kr/system/login/login.do")
        time.sleep(2)

        # ✅ 랜덤 ID 회피: placeholder 기반 셀렉터
        username_input = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
        password_input = driver.find_element(By.CSS_SELECTOR, "input[type='password']")

        username_input.send_keys(username)
        password_input.send_keys(password)
        
        # 로그인 버튼 클릭
        driver.find_element(By.CSS_SELECTOR, "button[onclick*='doLogin']").click()
        
        # login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        # login_button.click()

        update_status(status_label, "로그인 시도 중...")
        time.sleep(3)

        # 로그인 후 강의 페이지 이동
        driver.get("https://www.neti.go.kr/lh/ms/cs/atnlcListView.do?menuId=1000006046")
        update_status(status_label, "강의실 접속 완료!")

    except Exception as e:
        messagebox.showerror("에러", f"로그인 실패:\n{str(e)}")
        update_status(status_label, "에러 발생")
    finally:
        pass  # driver.quit()을 생략하면 브라우저 유지됨

# ---------------- 설정 저장/불러오기 ----------------
def load_config():
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {"center": "경북", "username": "", "password": ""}

def save_config(center, username, password):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump({"center": center, "username": username, "password": password}, f, ensure_ascii=False)

# ---------------- 상태 업데이트 ----------------
def update_status(label, text):
    label.config(text=text)

# ---------------- UI 구성 ----------------
root = tk.Tk()
root.title("FairySeti AutoLogin")
root.geometry("300x360")
root.resizable(False, False)

config = load_config()

tk.Label(root, text="연수원 선택:").place(x=20, y=20)
center_combo = ttk.Combobox(root, values=["경북", "서울", "경기"], state="readonly")
center_combo.set(config.get("center", "경북"))
center_combo.place(x=110, y=20)

tk.Label(root, text="아이디:").place(x=20, y=60)
id_entry = tk.Entry(root)
id_entry.insert(0, config.get("username", ""))
id_entry.place(x=110, y=60)

tk.Label(root, text="비밀번호:").place(x=20, y=100)
pw_entry = tk.Entry(root, show="*")
pw_entry.insert(0, config.get("password", ""))
pw_entry.place(x=110, y=100)

status_label = tk.Label(root, text="대기 중...", font=("Arial", 11))
status_label.place(x=110, y=160)

def on_run():
    center = center_combo.get()
    username = id_entry.get()
    password = pw_entry.get()

    if not username or not password:
        messagebox.showwarning("입력 오류", "아이디와 비밀번호를 입력하세요.")
        return

    save_config(center, username, password)
    update_status(status_label, "자동 실행 중...")

    threading.Thread(target=lambda: run_automation(center, username, password, status_label)).start()

# 버튼
tk.Button(root, text="실행", width=10, command=on_run).place(x=60, y=220)
tk.Button(root, text="종료", width=10, command=lambda: root.quit()).place(x=160, y=220)

tk.Label(root, text="☕ 후원: Buy me a coffee", fg="gray").place(x=70, y=300)

root.mainloop()
