from movie_storage import movie_storage_sql as storage
import countryflag

HTML_TEMPLATE_FILE = '_static/index_template.html'
NEW_HML_FILE = 'web/index.html'
TITLE_REPLACE_STRING = "__TEMPLATE_TITLE__"
CONTENT_REPLACE_STRING = "__TEMPLATE_MOVIE_GRID__"

IMDB_URL = "https://www.imdb.com/title/"


def save_website(content, user):
    """ Writes an HTML file """
    try:
        with open(f"web/{user}.html", 'w') as file:
            file.write(content)
        print("Website was generated successfully.")
    except OSError:
        print("File could not be opened")


def load_template():
    """ Loads an HTML template file """
    with open(HTML_TEMPLATE_FILE, "r") as html_data:
        html_content = html_data.read()
        return html_content


def serialize_movies(user):
    movies = storage.load_movies(user)
    html_string = ""
    if not movies:
        html_string += "<h1>Quite empty here, huh?</h1>"
    else:
        for movie, data in movies.items():
            poster = data['poster']
            title = movie
            year = data['year']
            country = []
            countries = data['country']
            country.append(countries.split(", ")[-1])
            note = data['notes']
            rating = data['rating']
            imdb_id = data['imdb_id']
            if note == "" or note is None:
                note = title
            flag = countryflag.getflag(country)
            html_string += f"<li>\n<div class='movie'>\n"
            html_string += f"<a href='{IMDB_URL}{imdb_id}' target='_blank'>\n"
            html_string += f"<img class='movie-poster' src='{poster}' title='{note}'\\>\n</a>"
            html_string += f"<div class='movie-title'>{title} {flag}</div>\n"
            html_string += f"<div class='movie-year'>{year}</div>\n"
            html_string += f"<p class='movie-rating'>IMDB-rating: <b>{rating}</b></p>\n"
            html_string += f"</div>\n</li>\n"
    return html_string


def generate_html(user):
    template = load_template()
    movies_as_html = serialize_movies(user)
    template = template.replace(TITLE_REPLACE_STRING, f"{user}'s favourite movies collection 🎥")
    final_html_code = template.replace(CONTENT_REPLACE_STRING, movies_as_html)
    save_website(final_html_code, user)
