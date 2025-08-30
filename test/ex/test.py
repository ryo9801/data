import streamlit as st

# セッション状態を使ってページ遷移
if 'page' not in st.session_state:
    st.session_state.page = 'ホーム'

# ページ選択のためのボタン
if st.button("ホーム"):
    st.session_state.page = 'ホーム'
elif st.button("プロフィール"):
    st.session_state.page = 'プロフィール'
elif st.button("設定"):
    st.session_state.page = '設定'

# 現在のページに基づいてコンテンツを表示
if st.session_state.page == 'ホーム':
    st.title("ホームページ")
    st.write("こちらはホームページです。")

elif st.session_state.page == 'プロフィール':
    st.title("プロフィールページ")
    st.write("こちらはプロフィールページです。")

elif st.session_state.page == '設定':
    st.title("設定ページ")
    st.write("こちらは設定ページです。")
