import streamlit as st
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# ---------- secrets.toml에서 설정 불러오기 ----------
try:
    center = st.secrets["neti"]["center"]
    username = st.secrets["neti"]["username"]
    password = st.secrets["neti"]["password"]
except KeyError as e:
    st.error(f"❌ secrets.toml 설정이 누락되었습니다: {e}")
    st.stop()

# ---------- 자동화 실행 함수 ----------
def run_automation(center, username, password):
    try:
        st.info("브라우저 준비 중...")

        options = Options()
        options.add_argument("--headless")  # Streamlit Cloud 환경에서 필수
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

        st.info("로그인 페이지 접속 중...")
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

        # 강의실 페이지 접속
        driver.get("https://www.neti.go.kr/lh/ms/cs/atnlcListView.do?menuId=1000006046")
        st.success("✅ 강의실 접속 완료!")

    except Exception as e:
        st.error(f"🚫 자동화 중 오류 발생: {str(e)}")

# ---------- Streamlit UI ----------
st.set_page_config(page_title="FairySeti", page_icon="🧚", layout="centered")
st.title("🧚 FairySeti 자동 로그인 도우미")

st.write("`.streamlit/secrets.toml`에 저장된 계정 정보를 이용하여 자동 로그인합니다.")

st.markdown(f"🔐 현재 설정된 연수원: **{center}**")

if st.button("🚀 자동 로그인 실행"):
    run_automation(center, username, password)

st.markdown("---")
st.caption("© 2025 FairySeti | Streamlit 기반 자동화 도우미")
