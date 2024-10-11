# mapper.py
import sys

# Load the list of years from the years.txt file
years = []
with open("years.txt") as f:
    for line in f:
        years.extend(line.strip().split())

# Mapper function
for line in sys.stdin:
    line = line.strip()
    fields = line.split()
    
    if len(fields) == 5:
        reviewer_id, movie_title, genres, year, rating = fields
        rating = float(rating)
        
        # Filter out movies not in the specified years
        if year in years:
            genres = genres.split("|")
            for genre in genres:
                print(f"{year}\t{genre}\t{movie_title}\t{rating}")