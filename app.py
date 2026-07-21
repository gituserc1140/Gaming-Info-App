import streamlit as st
import requests
import logging
import os

logging.basicConfig(level=logging.ERROR)
REPO_URL = os.getenv("RAWG_GITHUB_REPO_URL", "https://github.com/gituserc1140/RAWG-Games")
SPONSOR_URL = os.getenv("RAWG_GITHUB_SPONSOR_URL", "https://github.com/sponsors/gituserc1140")
REQUEST_TIMEOUT_SECONDS = 20
logger = logging.getLogger(__name__)

def fetch_games(api_key, query):
    url = "https://api.rawg.io/api/games"
    try:
        response = requests.get(
            url,
            params={"key": api_key, "search": query},
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
    except requests.RequestException:
        logger.exception("Network error while fetching games.")
        st.error("Network error while fetching games. Please check your connection and try again.")
        return []

    if response.status_code == 200:
        return response.json().get("results", [])

    if response.status_code in (401, 403):
        st.error("Invalid RAWG API key. Please check your key and try again.")
        return []

    st.error(f"Error fetching data: {response.status_code}")
    return []

def render_project_links():
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("GitHub Repository", REPO_URL, use_container_width=True)
    with col2:
        st.link_button("GitHub Sponsors", SPONSOR_URL, use_container_width=True)

GAMING_CSS = """
<style>
/* ── Base ───────────────────────────────────────────────────── */
html, body, .stApp, [data-testid="stAppViewContainer"],
[data-testid="stAppViewContainer"] > .main {
    background: radial-gradient(circle at top, #171736 0%, #0a0a14 48%, #06060f 100%) !important;
    color: #e0e0f0 !important;
}
[data-testid="stHeader"] {
    background-color: rgba(10, 10, 20, 0.85) !important;
}
[data-testid="stSidebar"] {
    background-color: #0d0d1e !important;
}

/* ── Typography ─────────────────────────────────────────────── */
h1, h2, h3, h4, h5, h6 {
    color: #00e5ff !important;
    text-shadow: 0 0 12px rgba(0, 229, 255, 0.55);
    font-family: 'Segoe UI', 'Arial', sans-serif;
    letter-spacing: 1px;
}
p, li, label, div {
    color: #c8c8e8 !important;
}

/* ── Inputs ─────────────────────────────────────────────────── */
div[data-baseweb="input"] input {
    background-color: #12122a !important;
    color: #e0e0f0 !important;
    border: 1px solid #7b2fff !important;
    border-radius: 6px !important;
}
div[data-baseweb="input"]:focus-within {
    border-color: #00e5ff !important;
    box-shadow: 0 0 8px rgba(0, 229, 255, 0.4) !important;
}

/* ── Buttons ────────────────────────────────────────────────── */
.stButton > button, button[kind="primary"], [data-testid="baseButton-primary"] {
    background: linear-gradient(135deg, #7b2fff, #00e5ff) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 6px !important;
    font-weight: 700 !important;
    letter-spacing: 0.5px;
    transition: opacity 0.2s;
}
button[kind="primary"]:hover, [data-testid="baseButton-primary"]:hover {
    opacity: 0.85 !important;
}
[data-testid="baseButton-secondary"], [data-testid="stLinkButton"] a {
    background-color: #12122a !important;
    color: #00e5ff !important;
    border: 1px solid #00e5ff !important;
    border-radius: 6px !important;
}

/* ── Info / Warning banners ─────────────────────────────────── */
[data-testid="stAlert"] {
    background-color: #12122a !important;
    border-left: 4px solid #7b2fff !important;
    color: #c8c8e8 !important;
    border-radius: 6px !important;
}

/* ── Dividers ───────────────────────────────────────────────── */
hr {
    border-color: #2a2a4a !important;
}

/* ── Game card text ─────────────────────────────────────────── */
[data-testid="stMarkdownContainer"] strong {
    color: #00e5ff !important;
}
</style>
"""

def main():
    st.set_page_config(page_title="RAWG Video Games Search", page_icon=":video_game:")
    st.markdown(GAMING_CSS, unsafe_allow_html=True)
    st.title("RAWG Video Games Search")
    render_project_links()

    api_key = st.text_input("Enter your RAWG API Key", type="password")
    query = st.text_input("Search for a game")
    if not api_key and not query:
        st.info("Enter your RAWG API key and a game name to enable search.")
    elif not api_key:
        st.info("Enter your RAWG API key to enable search.")
    elif not query:
        st.info("Enter a game name to enable search.")

    search_pressed = st.button("Search", disabled=not (api_key and query))

    if search_pressed:
        games = fetch_games(api_key, query)
        if games:
            for game in games:
                st.write(f"**{game.get('name', 'N/A')}**")
                if game.get("background_image"):
                    st.image(game["background_image"], width=200)
                st.write(f"Rating: {game.get('rating', 'N/A')}")
                st.write(f"Released: {game.get('released', 'N/A')}")
                st.write("---")
        else:
            st.warning("No games found.")

if __name__ == "__main__":
    main()