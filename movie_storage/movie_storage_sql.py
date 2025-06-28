from sqlalchemy import create_engine, text

# Define the database URL
DB_URL = "sqlite:///./data/movies.db"

# Create the engine
engine = create_engine(DB_URL, echo=False)

# Create the movies table if it does not exist
with engine.connect() as connection:
    connection.execute(text("""
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT UNIQUE NOT NULL,
            year INTEGER NOT NULL,
            rating REAL NOT NULL,
            poster TEXT NOT NULL
        )
    """))
    connection.commit()


def load_movies(user):
    """Retrieve all movies from the database."""
    with engine.connect() as connection:
        result = connection.execute(text("""SELECT title, year, rating, country, poster, notes, imdb_id FROM movies
                                         JOIN users ON users.id = movies.user_id WHERE users.name = :user"""),
                                            {"user": user})
        movies = result.fetchall()

    return {row[0]: {"year": row[1], "rating": row[2], "poster": row[4],
                     "notes": row[5], 'imdb_id': row[6], "country": row[3]} for row in movies}


def get_user_id(user):
    with engine.connect() as connection:
        try:
            result = connection.execute(text("""SELECT id FROM users WHERE name = :user"""),
                               {"user": user})
            connection.commit()
            user_id = result.fetchall()
            return user_id[0][0]
        except Exception as e:
            print(f"Error: {e}")


def add_movie(title, year, country, rating, poster, notes, imdb_id, user):
    """Add a new movie to the database."""
    user_id = get_user_id(user)
    with engine.connect() as connection:
        try:
            connection.execute(text("""INSERT INTO movies (title, year, country, rating, poster, notes, imdb_id, user_id) 
                                       VALUES (:title, :year, :country, :rating, :poster, :notes, :imdb_id, :user_id)"""),
                               {"title": title, "year": year, "country": country, "rating": rating,
                                "poster": poster, "notes": notes, 'imdb_id': imdb_id, 'user_id': user_id})
            connection.commit()
            print(f"Movie '{title}' added successfully to {user}'s collection.")
        except Exception as e:
            print(f"Error: {e}")


def delete_movie(title, user):
    """Delete a movie from the database."""
    user_id = get_user_id(user)
    with engine.connect() as connection:
        try:
            connection.execute(text("DELETE FROM movies WHERE LOWER(title) = LOWER(:title) AND user_id = :user_id"),
                                 {"title": title, "user_id": user_id})
            connection.commit()
            print(f"{title} has been successfully deleted.")
        except Exception as e:
            print(f"Error: {e}")


def update_movie(title, note, user):
    """Update a movie's rating in the database."""
    user_id = get_user_id(user)
    with engine.connect() as connection:
        try:
            connection.execute(text("UPDATE movies SET 'notes' = :note WHERE LOWER(title) = LOWER(:title) AND user_id = :user_id"),
                                {"title": title, "note": note, "user_id": user_id})
            connection.commit()
            print(f"{title}'s notes successfully set to '{note}'.")
        except Exception as e:
            print(f"Error: {e}")
