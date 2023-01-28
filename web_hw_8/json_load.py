import json

def get_authors_json(file_authors):
    with open(file_authors, "r") as fh:
        unpacked_authors = json.load(fh)
        #print(unpacked_authors)
    return unpacked_authors

def get_quotes_json(file_quotes):
    with open(file_quotes, "r") as fh:
        unpacked_quotes = json.load(fh)
        print(type(unpacked_quotes))
    return unpacked_quotes


if __name__ == "__main__":
    file_authors = 'authors.json'
    file_quotes = 'quotes.json'

    get_authors_json(file_authors)
    get_quotes_json(file_quotes)