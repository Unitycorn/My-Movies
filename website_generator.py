from movie_storage import movie_storage_sql as storage

HTML_TEMPLATE_FILE = '_static/index_template.html'
NEW_HML_FILE = 'web/index.html'
TITLE_REPLACE_STRING = "__TEMPLATE_TITLE__"
CONTENT_REPLACE_STRING = "__TEMPLATE_MOVIE_GRID__"


def save_website(content):
    """ Writes an HTML file """
    try:
        with open(NEW_HML_FILE, 'w') as file:
            file.write(content)
        print("Website was generated successfully.")
    except OSError:
        print("File could not be opened")


def load_template():
    """ Loads an HTML template file """
    with open(HTML_TEMPLATE_FILE, "r") as html_data:
        html_content = html_data.read()
        return html_content


def serialize_movies():
    movies = storage.load_movies()
    html_string = ""
    for movie, data in movies.items():
        poster = data['poster']
        title = movie
        year = data['year']
        html_string += f"<li>\n<div class='movie'>\n"
        html_string += f"<img class='movie-poster' src='{poster}'\\>\n"
        html_string += f"<div class='movie-title'>{title}</div>\n"
        html_string += f"<div class='movie-year'>{year}</div>\n"
        html_string += f"</div>\n</li>\n"
    return html_string


def generate_html():
    template = load_template()
    movies_as_html = serialize_movies()
    template = template.replace(TITLE_REPLACE_STRING, "My favourite movies")
    final_html_code = template.replace(CONTENT_REPLACE_STRING, movies_as_html)
    save_website(final_html_code)
