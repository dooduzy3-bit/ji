import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(
    page_title="목일중학교 게시판",
    page_icon="📌",
    layout="centered"
)

st.title("📌 목일중학교 게시판")

DATA_FILE = "posts.csv"

# 게시글 파일 없으면 생성
if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=["제목", "내용", "작성자", "작성일"])
    df.to_csv(DATA_FILE, index=False)

# 데이터 불러오기
df = pd.read_csv(DATA_FILE)

menu = st.sidebar.selectbox("메뉴", ["게시글 보기", "게시글 작성"])

# -----------------------
# 게시글 보기
# -----------------------
if menu == "게시글 보기":
    st.subheader("📄 게시글 목록")

    if df.empty:
        st.info("아직 게시글이 없습니다.")
    else:
        for i in range(len(df)-1, -1, -1):
            with st.expander(f"📌 {df.loc[i, '제목']}"):
                st.write(f"**작성자:** {df.loc[i, '작성자']}")
                st.write(f"**작성일:** {df.loc[i, '작성일']}")
                st.markdown("---")
                st.write(df.loc[i, "내용"])

# -----------------------
# 게시글 작성
# -----------------------
elif menu == "게시글 작성":
    st.subheader("✏️ 게시글 작성")

    title = st.text_input("제목")
    content = st.text_area("내용", height=150)
    writer = st.text_input("작성자")

    if st.button("등록"):
        if title and content and writer:
            new_post = {
                "제목": title,
                "내용": content,
                "작성자": writer,
                "작성일": datetime.now().strftime("%Y-%m-%d %H:%M")
            }
            df = pd.concat([df, pd.DataFrame([new_post])], ignore_index=True)
            df.to_csv(DATA_FILE, index=False)

            st.success("게시글이 등록되었습니다!")
            st.experimental_rerun()
        else:
            st.warning("모든 항목을 입력해주세요.")
