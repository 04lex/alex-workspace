import couchdb

# creds
couchdb_url = 'http://localhost:5984'
username = 'admin'
password = 'admin'

# conn
server = couchdb.Server(couchdb_url)
server.resource.credentials = (username, password)

# conn to db
db_name = 'moviesdb'
if db_name in server:
    db = server[db_name]
else:
    db = server.create(db_name)

# insert new movie doc
movie_data = {
    "title": "The Matrix",
    "genre": "Sience Fiction",
    "release_year": 1999
}

# save doc
doc_id, doc_rev = db.save(movie_data)
print(f'Document with ID {doc_id} inserted.')

# query by title
view_result = db.view('movies/by_title', include_docs=True)
for row in view_result:
    movie_doc = row.doc
    print(f"Title: {movie_doc['title']}, Genre: {movie_doc['genre']}, Year: {movie_doc['release_year']}")