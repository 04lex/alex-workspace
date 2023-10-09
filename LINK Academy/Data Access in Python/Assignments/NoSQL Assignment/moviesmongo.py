from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['moviesdb']

movies_collection = db['Movies']

movies_to_insert = [
    {
        "title": "The Matrix",
        "genre": "Science Fiction",
        "release_year": 1999
    },
    # {}
]

# insert movies_to_insert in movies_collection
movies_collection.insert_many(movies_to_insert)

# read
all_movies = movies_collection.find()

for movie in all_movies:
    print(f"Title: {movie['title']}, Genre: {movie['genre']}, Release year: {movie['release_year']}")
          
client.close()