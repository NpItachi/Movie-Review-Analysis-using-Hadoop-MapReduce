# combiner.py
import sys

# Combiner function
current_key = None
total_rating = 0
num_ratings = 0
movie_title = None

for line in sys.stdin:
    line = line.strip()
    key, genre, title, rating = line.split("\t", 3)
    rating = float(rating)
    
    if current_key is None:
        current_key = key
    
    if current_key == key:
        total_rating += rating
        num_ratings += 1
        movie_title = title
    else:
        if num_ratings > 0:
            avg_rating = total_rating / num_ratings
            print(f"{current_key}\t{genre}\t{movie_title}\t{avg_rating}\t{num_ratings}")
        
        current_key = key
        total_rating = rating
        num_ratings = 1
        movie_title = title

if num_ratings > 0:
    avg_rating = total_rating / num_ratings
    print(f"{current_key}\t{genre}\t{movie_title}\t{avg_rating}\t{num_ratings}")