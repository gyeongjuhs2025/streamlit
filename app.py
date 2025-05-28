<<<<<<< HEAD
import streamlit as st
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

CONFIG_FILE = "config.json"

# ---------- 설정 저장 및 불러오기 ----------
def load_config():
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {"center": "경북", "username": "", "password": ""}

def save_config(center, username, password):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump({"center": center, "username": username, "password": password}, ensure_ascii=False)

# ---------- 자동화 실행 함수 ----------
def run_automation(center, username, password):
    try:
        st.info("브라우저 준비 중...")

        options = Options()
        options.add_argument("--headless")  # Streamlit Cloud에서 필요
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

        st.info("로그인 페이지로 이동 중...")
        driver.get("https://www.neti.go.kr/system/login/login.do")
        time.sleep(2)

        # 아이디, 비밀번호 입력
        username_input = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
        password_input = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
        username_input.send_keys(username)
        password_input.send_keys(password)

        # 로그인 버튼 클릭
        driver.find_element(By.CSS_SELECTOR, "button[onclick*='doLogin']").click()
        st.info("로그인 시도 중...")
        time.sleep(3)

        # 강의실 페이지로 이동
        driver.get("https://www.neti.go.kr/lh/ms/cs/atnlcListView.do?menuId=1000006046")
        st.success("✅ 강의실 접속 완료!")

    except Exception as e:
        st.error(f"🚫 에러 발생: {str(e)}")

# ---------- Streamlit UI ----------
st.title("🧚 FairySeti 자동 로그인 도우미")

config = load_config()

st.write("NETI 연수원 자동 로그인 도우미입니다. 아이디와 비밀번호를 입력하고 실행 버튼을 눌러 주세요.")

center = st.selectbox("연수원 선택", ["경북", "서울", "경기"], index=["경북", "서울", "경기"].index(config.get("center", "경북")))
username = st.text_input("아이디", value=config.get("username", ""))
password = st.text_input("비밀번호", type="password", value=config.get("password", ""))

if st.button("🚀 자동 로그인 실행"):
    if username and password:
        save_config(center, username, password)
        run_automation(center, username, password)
    else:
        st.warning("아이디와 비밀번호를 모두 입력해 주세요.")

st.markdown("---")
st.caption("© 2025 FairySeti | Streamlit 기반 자동화 도우미")
=======
import streamlit as st
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

CONFIG_FILE = "config.json"

# ---------- 설정 저장 및 불러오기 ----------
def load_config():
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {"center": "경북", "username": "", "password": ""}

def save_config(center, username, password):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump({"center": center, "username": username, "password": password}, ensure_ascii=False)

# ---------- 자동화 실행 함수 ----------
def run_automation(center, username, password):
    try:
        st.info("브라우저 준비 중...")

        options = Options()
        options.add_argument("--headless")  # Streamlit Cloud에서 필요
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

        st.info("로그인 페이지로 이동 중...")
        driver.get("https://www.neti.go.kr/system/login/login.do")
        time.sleep(2)

        # 아이디, 비밀번호 입력
        username_input = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
        password_input = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
        username_input.send_keys(username)
        password_input.send_keys(password)

        # 로그인 버튼 클릭
        driver.find_element(By.CSS_SELECTOR, "button[onclick*='doLogin']").click()
        st.info("로그인 시도 중...")
        time.sleep(3)

        # 강의실 페이지로 이동
        driver.get("https://www.neti.go.kr/lh/ms/cs/atnlcListView.do?menuId=1000006046")
        st.success("✅ 강의실 접속 완료!")

    except Exception as e:
        st.error(f"🚫 에러 발생: {str(e)}")

# ---------- Streamlit UI ----------
st.title("🧚 FairySeti 자동 로그인 도우미")

config = load_config()

st.write("NETI 연수원 자동 로그인 도우미입니다. 아이디와 비밀번호를 입력하고 실행 버튼을 눌러 주세요.")

center = st.selectbox("연수원 선택", ["경북", "서울", "경기"], index=["경북", "서울", "경기"].index(config.get("center", "경북")))
username = st.text_input("아이디", value=config.get("username", ""))
password = st.text_input("비밀번호", type="password", value=config.get("password", ""))

if st.button("🚀 자동 로그인 실행"):
    if username and password:
        save_config(center, username, password)
        run_automation(center, username, password)
    else:
        st.warning("아이디와 비밀번호를 모두 입력해 주세요.")

st.markdown("---")
st.caption("© 2025 FairySeti | Streamlit 기반 자동화 도우미")