import streamlit as st
import requests

def fetch_games(api_key, query):
    url = f"https://api.rawg.io/api/games?key={api_key}&search={query}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        st.error(f"Error fetching data: {response.status_code}")
        return []

def main():
    st.title("RAWG Video Games Search")
    api_key = st.text_input("Enter your RAWG API Key", type="password")
    query = st.text_input("Search for a game")

    if st.button("Search") and api_key and query:
        games = fetch_games(api_key, query)
        if games:
            for game in games:
                st.write(f"**{game['name']}**")
                st.image(game['background_image'], width=200)
                st.write(f"Rating: {game['rating']}")
                st.write(f"Released: {game['released']}")
                st.write("---")
        else:
            st.warning("No games found.")

if __name__ == "__main__":
    main()