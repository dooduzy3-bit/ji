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

# 파일 생성
if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=["제목", "내용", "작성자", "작성일"])
    df.to_csv(DATA_FILE, index=False)

df = pd.read_csv(DATA_FILE)

menu = st.sidebar.selectbox(
    "메뉴",
    ["게시글 보기", "게시글 작성", "내 글 수정/삭제"]
)

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

# -----------------------
# 내 글 수정 / 삭제
# -----------------------
elif menu == "내 글 수정/삭제":
    st.subheader("🛠 내 글 수정 / 삭제")

    my_name = st.text_input("작성자 이름을 입력하세요")

    my_posts = df[df["작성자"] == my_name]

    if my_name == "":
        st.info("이름을 입력해주세요.")
    elif my_posts.empty:
        st.warning("작성한 글이 없습니다.")
    else:
        post_index = st.selectbox(
            "수정/삭제할 글 선택",
            my_posts.index,
            format_func=lambda x: df.loc[x, "제목"]
        )

        new_title = st.text_input(
            "제목 수정",
            df.loc[post_index, "제목"]
        )
        new_content = st.text_area(
            "내용 수정",
            df.loc[post_index, "내용"],
            height=150
        )

        col1, col2 = st.columns(2)

        with col1:
            if st.button("수정하기"):
                df.loc[post_index, "제목"] = new_title
                df.loc[post_index, "내용"] = new_content
                df.to_csv(DATA_FILE, index=False)
                st.success("게시글이 수정되었습니다!")
                st.experimental_rerun()

        with col2:
            if st.button("삭제하기"):
                df = df.drop(post_index)
                df.to_csv(DATA_FILE, index=False)
                st.success("게시글이 삭제되었습니다!")
                st.experimental_rerun()
