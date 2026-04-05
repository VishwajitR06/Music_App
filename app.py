import streamlit as st
import pandas as pd

# Load the song dataset
df = pd.read_csv("songs.csv")

st.set_page_config(page_title="🎵 Music Recommendation System", layout="centered")

st.title("🎶 Music Recommendation System")

# Sidebar filters
st.sidebar.header("Filter Songs")

genre_options = ["All"] + sorted(df["Genre"].unique())
artist_options = ["All"] + sorted(df["Artist"].unique())

selected_genre = st.sidebar.selectbox("Select Genre", genre_options)
selected_artist = st.sidebar.selectbox("Select Artist", artist_options)

# Filter logic
filtered_df = df.copy()

if selected_genre != "All":
    filtered_df = filtered_df[filtered_df["Genre"] == selected_genre]

if selected_artist != "All":
    filtered_df = filtered_df[filtered_df["Artist"] == selected_artist]

# Display results
st.subheader("🎧 Suggested Songs")
if filtered_df.empty:
    st.warning("No songs match your criteria.")
else:
    for index, row in filtered_df.iterrows():
        st.write(f"**{row['Song']}** by *{row['Artist']}* — _{row['Genre']}_")
