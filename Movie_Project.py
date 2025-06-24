# from colorama import Fore
from random import randint
from statistics import median, mean


def display_main_menu():
    """Output of the main navigation"""
    print()
    print("Menu:")
    print("0. Exit")
    print("1. List movies")
    print("2. Add movie")
    print("3. Delete movie")
    print("4. Update movie")
    print("5. Stats")
    print("6. Random movie")
    print("7. Search movie")
    print("8. Movies sorted by rating")
    print()


def create_sorted_movie_list(movies):
    """Creates a list of movie data tuples and sorts the list by rating"""
    movie_list = []
    for movie in movies:
        movie_list.append((movie['title'], movie['data']['rating'], movie['data']['year']))
    movie_list.sort(key=lambda tup: tup[1], reverse=True)  # sort by rating, descending
    return movie_list


def print_random_movie(movies):
    """Selects a random movie from a sorted list and prints its infos"""
    my_movie_list = create_sorted_movie_list(movies)
    selection = randint(0, len(my_movie_list)-1)
    selected_movie = my_movie_list[selection]
    print()
    print("Your random movie: ")
    print(f"Title: {selected_movie[0]}\nRating: {selected_movie[1]}\nYear: {selected_movie[2]}")


def execute_user_input(input_string, movies):
    """Function dispatcher"""
    function_dict = {'1': list_movies, '2': add_movie, '3': delete_movie, '4': update_movie,
                     '5': print_stats, '6': print_random_movie, '7': search_movie, '8': print_sorted_movies}
    function_dict[input_string](movies)


def print_sorted_movies(movies):
    """Prints a sorted list of movies by rating, descending"""
    my_movie_list = create_sorted_movie_list(movies)
    print("\nMovies sorted by rating:\n")
    for movie in my_movie_list:
        print(f"Title: {movie[0]}\nRating: {movie[1]}\nYear: {movie[2]}\n")


def search_movie(movies):
    """Compares the movie titles with a given string and printing matching movies"""
    print()
    search_term = input("Enter part of movie name: ")
    print("\nFound movie(s):\n")
    for movie in movies:
        if search_term.lower() in movie['title'].lower():
            print(f"{movie['title']}, Rating: {movie['data']['rating']}, Year: {movie['data']['year']}")


def list_movies(movies):
    """List all movies in the database (unsorted) and the total of movies in the db"""
    print()
    print(f"{len(movies)} in total")
    print()
    for movie in movies:
        print(f"{movie['title']}\nRating: {movie['data']['rating']}\nYear: {movie['data']['year']}\n")


def add_movie(movies):
    """Add a new movie to the database"""
    print()
    movie = input("Please enter the movie title: ")
    rating = float(input("Please enter the rating: "))
    year = input("Please enter the year: ")
    movies.append({'title': movie, 'data': {'rating': rating, 'year': year}})


def delete_movie(movies):
    """Delete a movie from the database"""
    print()
    movie_to_delete = input("Please enter a movie to delete: ")
    for movie in movies:
        if movie_to_delete == movie['title']:
            del movies[movies.index(movie)]
            print(f"\n{movie['title']} deleted")
            return
    print("Error: movie not in database")


def update_movie(movies):
    """Update a movies rating"""
    print()
    movie_to_update = input("Please enter a movie to update rating: ")
    for movie in movies:
        if movie_to_update in movie['title']:
            new_rating = input("Please enter new rating: ")
            movies[movies.index(movie)]['data']['rating'] = new_rating
            return
    print("Error: movie not in database")


def print_best_worst_movie(my_movie_list):
    """Looks for the best and worst rating in the movies list, only the first occurrence is shown"""
    best_movie_rating = 0.0
    worst_movie_rating = 10.0
    for movie in my_movie_list:
        if movie[1] > best_movie_rating:
            best_movie_rating = movie[1]
        if movie[1] < worst_movie_rating:
            worst_movie_rating = movie[1]
    for movie in my_movie_list:
        if movie[1] == best_movie_rating:
            print(f"\nBest rated movie:\n{movie[0]}, Rating: {movie[1]}, Year: {movie[2]}")
        if movie[1] == worst_movie_rating:
            print(f"\nWorst rated movie:\n{movie[0]}, Rating: {movie[1]}, Year: {movie[2]}")


def print_stats(movies):
    """Prints statistics about the movies based on ratings"""
    my_movie_list = create_sorted_movie_list(movies)
    ratings = []
    for movie in my_movie_list:
        rating = movie[1]
        ratings.append(rating)
    print("\nMovie statistics:\n")
    print(f"Average rating: {mean(ratings)}")
    print(f"Median rating: {median(ratings)}")
    print_best_worst_movie(my_movie_list)


def main():
    # Dictionary to store the movies and the rating
    movies = [
      {
        "title": "The Shawshank Redemption",
        "data": {"rating": 9.5, "year": "1987"}
      },
      {
        "title": "Pulp Fiction",
        "data": {"rating": 8.8, "year": "1987"}
      },
      {
        "title": "The Room",
        "data": {"rating": 3.6, "year": "1987"}
      },
      {
        "title": "The Godfather",
        "data": {"rating": 9.2, "year": "1987"}
      },
      {
        "title": "The Godfather: Part II",
        "data": {"rating": 9.0, "year": "1987"}
      },
      {
        "title": "The Dark Knight",
        "data": {"rating": 9.0, "year": "1987"}
      },
      {
        "title": "12 Angry Men",
        "data": {"rating": 8.9, "year": "1987"}
      },
      {
        "title": "Everything Everywhere All At Once",
        "data": {"rating": 8.9, "year": "1987"}
      },
      {
        "title": "Forrest Gump",
        "data": {"rating": 8.8, "year": "1987"}
      },
      {
        "title": "Star Wars: Episode V",
        "data": {"rating": 8.7, "year": "1987"}
      },
    ]

    app_title = "My Movies Database"

    print(f"{'*'*10} {app_title} {'*'*10}")
    while True:
        display_main_menu()
        user_input = input("Enter choice (0-8): ")
        if user_input != "0":
            execute_user_input(user_input, movies)
            print()
            input("Press enter to continue...")
        elif user_input == "0":
            print("Bye!")
            return True


if __name__ == "__main__":
    main()
