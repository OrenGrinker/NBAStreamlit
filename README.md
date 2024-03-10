# NBA Games Viewer

A Streamlit application to view NBA games and news, showcasing modularity in Python code organization.

## Features

- View NBA games by date with team logos.
- Fetch and display the latest NBA news.
- Modular Python codebase for better organization and maintenance.

## Installation

First, clone the repository:

```bash
git clone https://github.com/OrenGrinker/NBAStreamlit
cd NBAStreamlit
```
Then, install the required dependencies:
```bash
pip install -r requirements.txt
```
## API Key

To fetch NBA data, you need an API key from Sportsdata.io:

- Visit Sportsdata.io.
- Register for an account and log in.
- Navigate to the API keys section and generate a new API key for the NBA API.

## Project Structure

- app.py: The main Streamlit application file.
- nba_utils.py: Contains utility functions for fetching and displaying NBA games and news.
- team_logos.py: Holds the dictionary mapping team abbreviations to their logo URLs.
Usage

Run the Streamlit application:
```bash
streamlit run app.py
```

Enter your API key in the sidebar within the app to start fetching NBA games and news data.

## Screenshot
https://raw.githubusercontent.com/OrenGrinker/NBAStreamlit/main/Screenshot%202024-03-10%20at%2017.39.22.png
