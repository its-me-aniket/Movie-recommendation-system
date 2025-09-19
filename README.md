# Movie Recommender System

This project is a content-based movie recommender system that suggests movies similar to a user's selection. The application is built using Python, and the user interface is created with Streamlit.

## How it Works

The recommendation engine is built on the principles of content-based filtering.

1.  **Data Collection**: The project uses the TMDB 5000 movie dataset, which contains information about 5000 movies, including details like overview, genres, keywords, cast, and crew.

2.  **Feature Engineering**: Key features for each movie (overview, genres, keywords, cast, and director) are combined to create a consolidated 'tags' feature. This feature represents the movie's content profile.

3.  **Text Vectorization**: The textual 'tags' are converted into a numerical format using the **Bag-of-Words** technique (`CountVectorizer`). This process creates a vector for each movie in a high-dimensional space.

4.  **Similarity Calculation**: The **cosine similarity** is calculated between the vectors of all movies. The resulting similarity score quantifies how alike any two movies are based on their content.

5.  **Recommendation**: When a user selects a movie, the system identifies the top 5 movies with the highest similarity scores to the selected movie and presents them as recommendations.

The application also fetches and displays movie posters using the TMDB API to provide a richer user experience.

## Technologies Used

*   **Python**: Core programming language.
*   **Pandas & NumPy**: For efficient data manipulation and numerical operations.
*   **Scikit-learn**: For text vectorization (`CountVectorizer`) and similarity calculation (`cosine_similarity`).
*   **NLTK**: For natural language processing tasks like stemming.
*   **Streamlit**: To create and serve the interactive web application.
*   **Requests**: To fetch movie poster data from the TMDB API.

## Setup and Usage

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

5.  Open your web browser and navigate to the local URL provided by Streamlit. Select a movie from the dropdown menu and click the "Recommend" button to see the suggestions.
