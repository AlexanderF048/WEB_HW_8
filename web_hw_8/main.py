
from json_load import get_authors_json, get_quotes_json
from db_models import Authors, Quotes
from db_connection import db

if __name__ == "__main__":

    db

    file_authors = 'authors.json'
    file_quotes = 'quotes.json'

    authors = get_authors_json(file_authors)
    quotes = get_quotes_json(file_quotes)

    for author in authors:
        Authors(fullname=author['fullname'], born_date=author['born_date'], born_location=author['born_location'],
                description=author['description']).save()

    for quote in quotes:
        Quotes(tags=quote['tags'], author=quote['author'], quote=quote['quote']).save()




