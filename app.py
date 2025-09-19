import streamlit as st
import pickle
import numpy as np

# Load the movie dataset and similarity matrix
movies_list = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies_list['title'].values

similarity = np.load('similarity.npy')

def get_recommendations(movie_name):
    # Get the index using numpy where
    indices = np.where(movies_list == movie_name)[0]
    
    if len(indices) == 0:
        return f"Movie '{movie_name}' not found."
    
    movie_index = indices[0]
    
    distances = similarity[movie_index]
    movie_indices = distances.argsort()[-6:-1][::-1]
    
    return movies_list[movie_indices]


st.title("Movie Recommendation System")

seleted_movie_name = st.selectbox(
    "Select a movie name:",
    movies_list,
    index=None,
    placeholder="Select a movie"
)

# st.button(label="Recommend")
if st.button(label="Recommend"):
    st.write("Recommendations for:", seleted_movie_name)
    recommendations = get_recommendations(seleted_movie_name)
    for movie in recommendations:
        st.write(movie)
else:
    st.write("Please select a movie to get recommendations.")
st.markdown("""
    This is a simple movie recommendation system built using Streamlit and machine learning techniques.
    Select a movie from the dropdown to get recommendations based on similar movies.
""")
st.sidebar.header("About")
st.sidebar.text("This app recommends movies based on your selection.")
st.sidebar.text("Built with Streamlit and machine learning.")
st.sidebar.text("Data sourced from a movie dataset.")
st.sidebar.text("Developed by [Aniket Chatterjee].")