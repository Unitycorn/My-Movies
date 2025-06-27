# My movies app 🎥
This app was developed in the SE program at Masterschool.

Its an CLI tool to list, add, delete movies from an SQLite database, show different statistics, find movie by title and get a random movie to enjoy your evening.

Newly added movies just require a title, the rest of the data gets fetched from [OMDb API](https://www.omdbapi.com/). (You need an API key, which is not provided in this repo)
## Key features 🔑
Techstack: Python, HTML5, CSS, SQLite, REST-APIs

CLI based tool

CRUD: Create, Read, Update, Delete.

Analytics: Top-rated movies, least-rated movies etc.

SQL Storage: Instead of saving movies in a JSON file (earlier version), SQLite was now used.

API Fetching: Information about the movies is fetched from an API.

Website Generation: A website is generated based on a HTML-template and filed with movies data from the db.
