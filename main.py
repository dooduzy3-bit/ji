import streamlit as st
import pandas as pd
from datetime import datetime
import os

# =========================
# 1. 페이지 설정 (맨 위)
# =========================
st.set_page_config(
    page_title="목일중학교 게시판",
    page_icon="📌",
    layout="centered"
)

# =========================
# 2. 비밀번호 화면
# =========================
PASSWORD = "12345"

if "login" not in st.session_state:
    st.session_state.login = False

if st.session_state.login == False:
    st.title("🔐 목일중학교 게시판")

    pw = st.text_input("비밀번호를 입력하세요", type="password")

    if st.button("입장"):
        if pw == PASSWORD:
            st.session_state.login = True
            st.experimental_rerun()
        else:
            st.error("비밀번호가 틀렸습니다.")

    # 🚫 여기서 끝 (아래 코드 실행 안 됨)
    st.stop()

# =========================
# 3. 게시판 (비번 통과 후)
# =========================
st.title("📌 목일중학교 게시판")

DATA_FILE = "posts.csv"

if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=["제목", "내용", "작성자", "작성일"])
    df.to_csv(DATA_FILE, index=False)

df = pd.read_csv(DATA_FILE)

menu = st.sidebar.selectbox(
    "메뉴",
    ["게시글 보기", "게시글 작성", "내 글 수정/삭제"]
)

# 게시글 보기
if menu == "게시글 보기":
    st.subheader("📄 게시글 목록")

    if df.empty:
        st.info("아직 게시글이 없습니다.")
    else:
        for i in range(len(df) - 1, -1, -1):
            with st.expander(f"📌 {d
