# RAWG-Games

Streamlit app for searching video games using the [RAWG API](https://rawg.io/apidocs).  
Users can enter their own API key directly in the app UI and search for games by name.

[![Sponsor me on GitHub](https://img.shields.io/badge/Sponsor%20me%20on-GitHub-EA4AAA?logo=githubsponsors&style=flat-square)](https://github.com/sponsors/gituserc1140)
[![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-181717?logo=github&style=flat-square)](https://github.com/gituserc1140/RAWG-Games)

## Features

- Enter RAWG API key on the frontend (password field)
- Search games by title
- View game cover, rating, and release date
- Helpful UI feedback for missing/invalid API keys
- Quick access buttons for GitHub and GitHub Sponsors inside the app UI

## Setup

1. Clone the repository: `git clone https://github.com/gituserc1140/RAWG-Games.git`
2. Move into the project: `cd RAWG-Games`
3. Install dependencies: `pip install -r requirements.txt`
4. Start the Streamlit app: `streamlit run app.py`

## How to use

1. Open the app in your browser after running Streamlit.
2. Paste your RAWG API key into **Enter your RAWG API Key**.
3. Type a game name into **Search for a game**.
4. Click **Search** to view results.

## Reference

This project follows a similar concept to:  
https://github.com/gituserc1140/TranscriptionApp
