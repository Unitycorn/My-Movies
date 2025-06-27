from movie_storage import movie_storage_sql as storage
import data_fetcher
from random import randint
from statistics import median, mean
import website_generator


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
    print("9. Generate website")
    print()


def generate_website():
    return website_generator.generate_html()


def create_sorted_movie_list(movies):
    """Creates a list of movie data tuples and sorts the list by rating"""
    movie_list = []
    for movie, data in movies.items():
        movie_list.append((movie, data['rating'], data['year']))
    movie_list.sort(key=lambda tup: tup[1], reverse=True)  # sort by rating, descending
    return movie_list


def print_random_movie():
    """Selects a random movie from a sorted list and prints its infos"""
    movies = storage.load_movies()
    my_movie_list = create_sorted_movie_list(movies)
    selection = randint(0, len(my_movie_list)-1)
    selected_movie = my_movie_list[selection]
    print()
    print("Your random movie: ")
    print(f"{selected_movie[0]} ({selected_movie[2]}): {selected_movie[1]}")


def execute_user_input(input_string):
    """Function dispatcher"""
    function_dict = {'1': list_movies, '2': add_movie, '3': delete_movie, '4': update_movie,
                     '5': print_stats, '6': print_random_movie, '7': search_movie, '8': print_sorted_movies,
                     '9': generate_website}
    if input_string in function_dict.keys():
        function_dict[input_string]()
    else:
        print("\nError: Wrong input!")


def print_sorted_movies():
    """Prints a sorted list of movies by rating, descending"""
    movies = storage.load_movies()
    my_movie_list = create_sorted_movie_list(movies)
    print("\nMovies sorted by rating:\n")
    for movie in my_movie_list:
        print(f"{movie[0]} ({movie[2]}): {movie[1]}")


def search_movie():
    """Compares the movie titles with a given string and printing matching movies"""
    movies = storage.load_movies()
    print()
    while True:
        search_term = input("Enter part of movie name: ")
        if search_term != '':
            break
        else:
            print("\nError: name must not be empty!\n")
    print("\nFound movie(s):\n")
    found_movies = 0
    for movie, data in movies.items():
        if search_term.lower() in movie.lower():
            print(f"{movie} ({data['year']}): {data['rating']}")
            found_movies += 1
    if found_movies == 0:
        print("\nNo movies found!\n")


def list_movies():
    """List all movies in the database (unsorted) and the total of movies in the db"""
    movies = storage.load_movies()
    print()
    print(f"{len(movies)} in total")
    print()
    for movie, data in movies.items():
        print(f"{movie} ({data['year']}): {data['rating']}")


def add_movie():
    """Adds a new movie to the database if it not already exists"""
    movies = storage.load_movies()
    print()
    while True:
        title_exists = False
        title = input("Please enter the movie title: ")
        if title != '':
            for movie in movies:
                if movie.lower() == title.lower():
                    title_exists = True
                    print("\nError: Movie already exists\n")
            if title_exists:
                continue
            else:
                break
        else:
            print("\nError: Title must not be empty!\n")
    movie_to_add = data_fetcher.fetch_data(title)
    if movie_to_add:
        title = movie_to_add["Title"]
        rating = movie_to_add["Ratings"][0]["Value"].split("/")[0]  # IMDB rating
        year = movie_to_add["Year"]
        poster = movie_to_add["Poster"]
        storage.add_movie(title, year, rating, poster)


def delete_movie():
    """Delete a movie from the database"""
    print()
    while True:
        movie_to_delete = input("Please enter a movie to delete: ").capitalize()
        if movie_to_delete != '':
            storage.delete_movie(movie_to_delete)
            break
        else:
            print("\nError: Title must not be empty!\n")


def update_movie(movies):
    """Update a movies rating"""
    new_rating = 0.0
    print()
    while True:
        movie_to_update = input("Please enter a movie to update rating: ")
        if movie_to_update == '':
            print("\nError: Title must not be empty!\n")
            continue
        else:
            movie_found = False
            for movie in movies:
                if movie_to_update.lower() == movie.lower():
                    movie_found = True
                    break
                if movies.index(movie) == len(movies) - 1:
                    print("\nError 404: Movie not found!\n")
            if not movie_found:
                continue
            try:
                new_rating = float(input("Please enter the new rating: "))
            except ValueError:
                print("\nError: Rating must be a number!\n")
                continue
            break
    storage.update_movie(movie_to_update, new_rating)


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
            print(f"\nBest rated movie:\n{movie[0]} ({movie[2]}): {movie[1]}")
        if movie[1] == worst_movie_rating:
            print(f"\nWorst rated movie:\n{movie[0]} ({movie[2]}): {movie[1]}")


def print_stats():
    """Prints statistics about the movies based on ratings"""
    movies = storage.load_movies()
    my_movie_list = create_sorted_movie_list(movies)
    ratings = []
    for movie in my_movie_list:
        rating = movie[1]
        ratings.append(rating)
    print("\nMovie statistics:\n")
    print(f"Average rating: " + "{:.1f}".format(mean(ratings)))
    print(f"Median rating: " + "{:.1f}".format(median(ratings)))
    print_best_worst_movie(my_movie_list)


def main():
    """Prints the app title and the menu, calls the chosen function from dispatcher until choice is '0'"""
    app_title = "My Movies Database"
    print(f"{'*'*10} {app_title} {'*'*10}")
    while True:
        display_main_menu()
        user_input = input("Enter choice (0-9): ")
        if user_input != "0":
            execute_user_input(user_input)
            print()
            input("Press enter to continue...")
        elif user_input == "0":
            print("Bye!")
            return


if __name__ == "__main__":
    main()
