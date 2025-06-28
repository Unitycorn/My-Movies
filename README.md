# My movies app 🎥
This app was developed in the SE program at Masterschool.

Its an CLI tool to list, add, delete movies from an SQLite database, show different statistics, find movie by title and get a random movie to enjoy your evening.

Newly added movies just require a title, the rest of the data gets fetched from [OMDb API](https://www.omdbapi.com/). (You need an API key, which is not provided in this repo)

This app also supports multiple users! Add/Select your profile and see data from your very own collection. Also, the website generation and some CL output is now personalized.

The website contains an overview from all of your movies with title, year and the IMDB rating. The movies poster is also included and links to the movies IMDB page. A little flag near the movies name hints to the movies origin country.

## Installation 💻

Simply clone this repo, run ```pip install -r requirements.txt``` and run ```python3 main.py```! 
## Key features 🔑
Techstack: Python, HTML5, CSS, SQLite, REST-APIs

CLI based tool

CRUD: Create, Read, Update, Delete.

Analytics: Top-rated movies, least-rated movies etc.

SQL Storage: Instead of saving movies in a JSON file (earlier version), SQLite was now used.

API Fetching: Information about the movies is fetched from an API.

Website Generation: A website is generated based on a HTML-template and filed with movies data from the db.

Multi-User-Support: Users can generate and manage their very own movie lists and their own HTML document