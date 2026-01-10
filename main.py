import streamlit as st

st.set_page_config(page_title="게임 로그인", layout="wide")

# =========================
# 세션 상태 초기화
# =========================
if "users" not in st.session_state:
    st.session_state.users = {"admin": "1234"}  # 기본 계정

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "login"  # login or signup

# =========================
# 우측 상단 회원가입 버튼
# =========================
col1, col2 = st.columns([8, 2])

with col2:
    if st.button("회원가입"):
        st.session_state.page = "signup"

st.markdown("---")

# =========================
# 로그인 페이지
# =========================
if st.session_state.page == "login" and not st.session_state.logged_in:
    st.title("🎮 게임 로그인")

    username = st.text_input("아이디")
    password = st.text_input("비밀번호", type="password")

    if st.button("로그인"):
        if username in st.session_state.users:
            if st.session_state.users[username] == password:
                st.session_state.logged_in = True
                st.success("로그인 성공!")
                st.rerun()
            else:
                st.error("비밀번호가 틀렸습니다.")
        else:
            st.error("존재하지 않는 아이디입니다.")

# =========================
# 회원가입 페이지
# =========================
elif st.session_state.page == "signup":
    st.title("📝 회원가입")

    new_username = st.text_input("새 아이디")
    new_password = st.text_input("새 비밀번호", type="password")
    confirm_password = st.text_input("비밀번호 확인", type="password")

    if st.button("가입하기"):
        if not new_username or not new_password:
            st.warning("모든 항목을 입력해주세요.")
        elif new_username in st.session_state.users:
            st.error("이미 존재하는 아이디입니다.")
        elif new_password != confirm_password:
            st.error("비밀번호가 일치하지 않습니다.")
        else:
            st.session_state.users[new_username] = new_password
            st.success("회원가입 완료! 로그인 해주세요.")
            st.session_state.page = "login"
            st.rerun()

    if st.button("로그인으로 돌아가기"):
        st.session_state.page = "login"
        st.rerun()

# =========================
# 로그인 성공 후 화면
# =========================
elif st.session_state.logged_in:
    st.title("✅ 로그인 완료")
    st.write("게임 로비로 이동할 준비 완료!")

    if st.button("로그아웃"):
        st.session_state.logged_in = False
        st.session_state.page = "login"
        st.rerun()
