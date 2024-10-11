# reducer.py
import sys

# Reducer function
current_key = None
max_avg_rating = 0
max_movie_titles = []
min_votes = 10  # Minimum number of votes required

for line in sys.stdin:
    line = line.strip()
    key, genre, movie_title, avg_rating, num_ratings = line.split("\t")
    avg_rating = float(avg_rating)
    num_ratings = int(num_ratings)
    
    if current_key is None:
        current_key = key
    
    if current_key == key:
        if num_ratings >= min_votes:
            if avg_rating > max_avg_rating:
                max_avg_rating = avg_rating
                max_movie_titles = [movie_title]
            elif avg_rating == max_avg_rating:
                max_movie_titles.append(movie_title)
    else:
        if max_movie_titles:
            for title in max_movie_titles:
                print(f"{current_key}\t{title}\t{max_avg_rating}")
        
        current_key = key
        max_avg_rating = avg_rating if num_ratings >= min_votes else 0
        max_movie_titles = [movie_title] if num_ratings >= min_votes else []

if max_movie_titles:
    for title in max_movie_titles:
        print(f"{current_key}\t{title}\t{max_avg_rating}")