import json


def get_movies():
    """
    Returns a list of dictionaries that
    contains the movies information in the database.

    The function loads the information from the JSON
    file and returns the data.
    """
    with open("data.json", "r") as handle:
        data = json.load(handle)
        handle.close()
        return data


def save_movies(movies):
    """
    Gets all your movies as an argument and saves them to the JSON file.
    """
    try:
        with open("data.json", "w") as handle:
            json.dump(movies, handle, indent=4)
            handle.close()
    except OSError:
        print("Couldn't open file.")


def add_movie(title, rating, year):
    """
    Adds a movie to the movies database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = get_movies()
    movies.append({'title': title, 'data': {'rating': rating, 'year': year}})
    save_movies(movies)


def delete_movie(title):
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = get_movies()
    for movie in movies:
        if title == movie['title']:
            del movies[movies.index(movie)]
            save_movies(movies)
            print(f"\n{movie['title']} deleted")
            return
    print("Error: movie not in database")


def update_movie(title, rating):
    """
    Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = get_movies()
    for movie in movies:
        if title in movie['title']:
            movies[movies.index(movie)]['data']['rating'] = rating
            save_movies(movies)
            print(f"\n{movie['title']} successfully updated!")
            return
