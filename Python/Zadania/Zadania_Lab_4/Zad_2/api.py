import csv
from pathlib import Path
from fastapi import FastAPI
from data import Movie, Links

app = FastAPI()
CSV_PATH_MOVIES = Path(__file__).parent / "database" / "movies.csv"
CSV_PATH_LINKS = Path(__file__).parent / "database" / "links.csv"


@app.get("/movies")
def read_movies():
    movies = []
    with open(CSV_PATH_MOVIES, "r", newline="", encoding="utf-8") as file_m:
        reader = csv.DictReader(file_m)
        for row in reader:
            movie = Movie(
                movie_id=int(row["movieId"]),
                title=row["title"],
                genres=row["genres"],
            )
            movies.append(movie)
    return movies

@app.get("/links")
def read_links():
    links = []
    with open(CSV_PATH_LINKS, "r", newline="", encoding="utf-8") as file_l:
        reader = csv.DictReader(file_l)
        for row in reader:
            link = Links(
                movie_id=int(row["movieId"]),
                imdb_id=row["imdbId"],
                tmdb_id=row["tmdbId"],
            )
            links.append(link)
    return links