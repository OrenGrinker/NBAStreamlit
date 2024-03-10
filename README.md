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

## Contributing

Contributions, issues, and feature requests are welcome!

## License

This project is MIT licensed.

## Screenshot

![NBAStreamlit Screenshot]([https://github.com/OrenGrinker/SlackNewsAPI/blob/636ff9336802a598e95b44c8736c2a6a3487fbe0/Screenshot%202024-03-02%20at%2019.31.08.png](https://github.com/OrenGrinker/NBAStreamlit/blob/main/Screenshot%202024-03-10%20at%2017.39.22.png)https://github.com/OrenGrinker/NBAStreamlit/blob/main/Screenshot%202024-03-10%20at%2017.39.22.png)

