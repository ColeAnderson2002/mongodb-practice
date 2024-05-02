#!/usr/bin/env python3

from pymongo import MongoClient, errors
import os
from db import *

# https://www.mongodb.com/docs/languages/python/pymongo-driver/current/ ; https://www.mongodb.com/resources/languages/python

db = client['kbv4nd'] # switches to my own db, which is computing id 

musicians = db['musicians'] # creating collection about musicians

musicians.delete_many({}) # clears out extra documents each time run 

musicians.insert_many([
  {"name": "John Mayer", "age": 46, "sex": "Male", "instrument_played": "Guitar", "genre": ["Blues", "Pop", "Rock"], "best_song": "Gravity"},
  {"name": "Alicia Keys", "age": 43, "sex": "Female", "instrument_played": ["Piano", "Vocals"], "genre": ["R&B", "Soul"], "best_song": "If I Ain't Got You'"},
  {"name": "Paul McCartney", "age": 81, "sex": "Male", "instrument_played": ["Bass Guitar", "Guitar", "Vocals"], "genre": ["Rock", "Pop"], "best_song": "Don't Let Me Down"},
  {"name": "Taylor Swift", "age": 34, "sex": "Female", "instrument_played": ["Guitar", "Piano", "Vocals"], "genre": ["Pop", "Country"], "best_song": "Love Story"},
  {"name": "Bruno Mars", "age": 38, "sex": "Male", "instrument_played": ["Vocals", "Guitar", "Piano"], "genre": ["Pop", "R&B", "Funk"], "best_song": "Locked Out of Heaven"}
]) # the 5 documents

# Querying to retreive 3 "documents" (musicians) over the age of 40
retrieve_musicians = musicians.find({"age": {"$gt": 40}})
for musician in retrieve_musicians:
    print(f'{musician}\n')

