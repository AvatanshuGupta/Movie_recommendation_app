import streamlit as st
import pandas as pd
import numpy as np
import requests

#Importing Data
new_df=pd.read_csv(r'Final_Data\new_df.csv')
similarity=pd.read_csv(r'Final_Data\similarity.csv')

#converting dataframe into numpy array
similarity=similarity.values

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path', '')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"
        else:
            return "https://via.placeholder.com/300x450.png?text=No+Image"
    except Exception as e:
        print(f"Error fetching poster for ID {movie_id}: {e}")
        return "https://via.placeholder.com/300x450.png?text=Error"



def recommend(movie):
    movie_index = new_df[new_df['title'] == movie].index[0]
    sorted_distance = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movie = []
    poster = []
    for i in sorted_distance:
        movie_id = new_df.iloc[i[0]]['movie_id']
        title = new_df.iloc[i[0]]['title']
        recommend_movie.append(title)
        poster.append(fetch_poster(movie_id))
    return recommend_movie, poster



st.title("Welcome to Movie recommendation App")


selected_movie=st.selectbox(label='Select a movie',
            options=new_df['title'].values
    )


if st.button("Recommend"):
    st.write("Top 5 Recommendations:")
    recommend_movie,poster=recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommend_movie[0])
        st.image(poster[0])
    with col2:
        st.text(recommend_movie[1])
        st.image(poster[1])
    with col3:
        st.text(recommend_movie[2])
        st.image(poster[2])
    with col4:
        st.text(recommend_movie[3])
        st.image(poster[3])
    with col5:
        st.text(recommend_movie[4])
        st.image(poster[4])        