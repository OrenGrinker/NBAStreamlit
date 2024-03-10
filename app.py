import streamlit as st
from datetime import datetime
import nba_utils

# Streamlit app title and sidebar setup
st.title('NBA Games Viewer')
st.sidebar.title('🏀 NBA Games & News 🏀')
api_key = st.sidebar.text_input("Enter your API Key")
page = st.sidebar.radio("Navigate", ['Games', 'News'])

# Main page navigation
if page == 'Games':
    nba_utils.games_page(api_key)
elif page == 'News':
    nba_utils.display_news(api_key)
