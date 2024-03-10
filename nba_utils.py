import streamlit as st
import requests
from datetime import datetime
from team_logos import team_logos

def display_team_logo(team):
    """Display team logo in the Streamlit app."""
    if team in team_logos:
        st.image(team_logos[team], width=50)
    else:
        st.write("Logo not found")

def fetch_and_display_games(api_key, url):
    """Fetch and display NBA games information."""
    if not api_key:
        st.write("Please enter your API key in the sidebar.")
        return

    response = requests.get(url)
    if response.status_code == 200:
        games = response.json()
        if games:
            for game in games:
                col1, col2, col3 = st.columns([1, 2, 1])
                with col1:
                    display_team_logo(game['AwayTeam'])
                with col2:
                    st.write(f"{game['AwayTeam']} at {game['HomeTeam']}")
                with col3:
                    display_team_logo(game['HomeTeam'])
                st.write(f"DateTime: {game['DateTime']}")
                st.markdown("---")
        else:
            st.write('No games found for this date.')
    else:
        st.write('Failed to retrieve data.')

def games_page(api_key):
    """Display games page with date input."""
    selected_date = st.date_input("Select a date", datetime.today())
    formatted_date = selected_date.strftime('%Y-%m-%d')
    games_url = f'https://api.sportsdata.io/v3/nba/scores/json/GamesByDate/{formatted_date}?key={api_key}'
    st.write(f'Games on {formatted_date}:')
    if selected_date:
        fetch_and_display_games(api_key, games_url)

def display_news(api_key):
    """Fetch and display NBA news."""
    if not api_key:
        st.write("Please enter your API key in the sidebar.")
        return

    news_url = f'https://api.sportsdata.io/v3/nba/scores/json/News?key={api_key}'
    response = requests.get(news_url)
    if response.status_code == 200:
        news_items = response.json()
        if news_items:
            for news in news_items:
                with st.container():
                    st.write(f"#### {news['Title']}")
                    st.write(f"{news['Content']}")
                    st.write(f"[Read more]({news['Url']})")
                    st.markdown("---")
        else:
            st.write('No news found.')
    else:
        st.write('Failed to retrieve news.')
