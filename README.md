
# Movie Recommendation System using NLP and TMDB Dataset

This project is a **Content-Based Movie Recommendation System** built using the **TMDB 5000 Movie Dataset**. It recommends similar movies based on a selected title by analyzing their content, including genres, keywords, cast, crew, and overview.
The application is built with **Streamlit** and features a clean UI where the user selects a movie and gets 5 recommended movies with posters.

## Technologies & Concepts Used

### Natural Language Processing (NLP)

- **Text Cleaning**: Lowercasing, removing spaces  
- **Text Normalization**: Stemming using `PorterStemmer` (NLTK)  
- **Tokenization**: Using Python’s built-in methods  
- **Vectorization**: `CountVectorizer` from scikit-learn with 5000 max features and English stopwords  
- **Similarity Calculation**: `cosine_similarity` from scikit-learn  

### Tools & Libraries

- `pandas`, `numpy` – for data manipulation  
- `scikit-learn` – for vectorization and similarity computation  
- `nltk` – for stemming  
- `Streamlit` – for creating the web interface  
- `requests` – for fetching movie posters using TMDB API  

## Dataset Description

### Source

- Data is taken from the [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

### Files Used

- `tmdb_5000_movies.csv`  
- `tmdb_5000_credits.csv`  

These files were merged and processed to extract:

- `movie_id`  
- `title`  
- `overview`  
- `genres`  
- `keywords`  
- `cast` (top 3 members)  
- `crew` (only the director)  

## Feature Engineering

### Steps:

1. Merging datasets on `title`  
2. Selecting features: `movie_id`, `title`, `overview`, `genres`, `keywords`, `cast`, `crew`  
3. Parsing JSON-like strings using `ast.literal_eval`  
4. Reducing cast to top 3 and crew to **director only**  
5. Combining all features into a single column `tags`  
6. Text cleaning and normalization (lowercase + stemming)  
7. Vectorizing text using `CountVectorizer`  
8. Calculating cosine similarity between movie vectors  

## Output Files

- `new_df.csv`: Contains only `movie_id`, `title`, and `tags` (processed)  
- `similarity.csv`: A 2D matrix containing pairwise cosine similarity scores  

## Web Application (Streamlit)

### Features:

- Movie title dropdown  
- Top 5 similar movie recommendations  
- Poster images fetched using TMDB API  

### API Used:

TMDB API to fetch poster images:

```
https://api.themoviedb.org/3/movie/{movie_id}?api_key=YOUR_API_KEY&language=en-US
```

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/AvatanshuGupta/Movie_recommendation_app.git
cd movie-recommender-nlp
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```
pandas
numpy
scikit-learn
nltk
streamlit
requests
```

### 3. Launch the App

```bash
streamlit run app.py
```

## Future Improvements

- Add collaborative filtering using user ratings  
- Improve NLP by using TF-IDF or word embeddings (like Word2Vec or BERT)  
- Deploy on cloud using platforms like Streamlit Cloud or Heroku  

## Acknowledgements

- Data Source: [TMDB on Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)  
- Poster API: [The Movie Database API](https://developers.themoviedb.org/3)  
- Inspiration: Content-based filtering via NLP  

