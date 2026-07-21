import streamlit as st
import requests

REPO_URL = "https://github.com/gituserc1140/RAWG-Games"
SPONSOR_URL = "https://github.com/sponsors/gituserc1140"

def fetch_games(api_key, query):
    url = "https://api.rawg.io/api/games"
    try:
        response = requests.get(
            url,
            params={"key": api_key, "search": query},
            timeout=20,
        )
    except requests.RequestException as exc:
        st.error(f"Network error while fetching games: {exc}")
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

def main():
    st.set_page_config(page_title="RAWG Video Games Search", page_icon="🎮")
    st.title("RAWG Video Games Search")
    render_project_links()

    api_key = st.text_input("Enter your RAWG API Key", type="password")
    query = st.text_input("Search for a game")
    search_clicked = st.button("Search")

    if search_clicked and not api_key:
        st.warning("Please enter your RAWG API key to search for games.")
        return

    if search_clicked and not query:
        st.warning("Please enter a game name to search.")
        return

    if search_clicked and api_key and query:
        games = fetch_games(api_key, query)
        if games:
            for game in games:
                st.write(f"**{game.get('name', 'Unknown title')}**")
                if game.get("background_image"):
                    st.image(game["background_image"], width=200)
                st.write(f"Rating: {game.get('rating', 'N/A')}")
                st.write(f"Released: {game.get('released', 'N/A')}")
                st.write("---")
        else:
            st.warning("No games found.")

if __name__ == "__main__":
    main()