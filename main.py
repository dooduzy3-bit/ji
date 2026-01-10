import streamlit as st
from datetime import datetime

st.set_page_config(page_title="학교 게시판", layout="centered")

st.title("🏫 학교 게시판")

# 게시글 저장 공간 (세션 상태)
if "posts" not in st.session_state:
    st.session_state.posts = []

# 사이드바 - 글 작성
st.sidebar.header("✏️ 글 작성")

title = st.sidebar.text_input("제목")
author = st.sidebar.text_input("작성자")
content = st.sidebar.text_area("내용")

if st.sidebar.button("등록"):
    if title and author and content:
        st.session_state.posts.append({
            "title": title,
            "author": author,
            "content": content,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        })
        st.sidebar.success("게시글이 등록되었습니다!")
    else:
        st.sidebar.warning("모든 항목을 입력해주세요.")

st.divider()

# 게시글 목록
st.subheader("📋 게시글 목록")

if not st.session_state.posts:
    st.info("아직 게시글이 없습니다.")
else:
    for idx, post in enumerate(reversed(st.session_state.posts)):
        with st.expander(f"{post['title']}  |  {post['author']}  ({post['date']})"):
            st.write(post["content"])
