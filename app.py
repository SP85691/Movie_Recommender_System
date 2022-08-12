# Import Dependencies
import streamlit as st
import pickle
import pandas as pd
import requests

# Fetching Poster with the help of TMDB-API
def fetch_poster(movie_id):
     response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=dd4868079838cb035ae80bf5f684a4fc&language=en-US'.format(movie_id))
     data = response.json()
     return "https://image.tmdb.org/t/p/w500/"+ data['poster_path']

# Creating Recommending System, which helps to return Movie Name and Movie Poster!
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        recommended.append(movies.iloc[i[0]].title)
        # Fetch Poster from API
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended, recommended_movies_poster

# Importing Pickle Files to accessing the Movie Data for Recommendation!
# Movie Dictionary
movie_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

# Similarity
similarity = pickle.load(open('similarity.pkl', 'rb'))

### Main Streamlit Format ###
#############################
# Head Title
st.title('Movie Recommender')

# Make Selection Box to Choose Movie Name!
option = st.selectbox(
    'How Would You Like to Contactes?',
    movies['title'].values)

# Creating Button!
if st.button('Recommend'):
    names, poster = recommend(option)

    # After Pressing Button Process:
    # The 5 Columns Output May Given by the API!

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(poster[0])

    with col2:
        st.text(names[1])
        st.image(poster[1])

    with col3:
        st.text(names[2])
        st.image(poster[2])

    with col4:
        st.text(names[3])
        st.image(poster[3])

    with col5:
        st.text(names[4])
        st.image(poster[4])

###### END OF THE PROGRAM ######