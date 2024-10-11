# Movie-Review-Analysis-using-Hadoop-MapReduce
This project focuses on analyzing movie review ratings to identify the best movies by year based on average rankings.

Movie Review Analysis using Hadoop MapReduce

**Description**

This project focuses on analyzing movie review ratings to identify the best movies by year based on average rankings. It uses Python-based Hadoop MapReduce with mapper, combiner, and reducer components to process a large dataset of movie reviews. The goal is to determine the movie title(s) with the highest average rank for each year, filtering based on specific criteria, such as release years listed in a separate file and a minimum number of ratings.

The data used includes over 100,000 ratings from multiple reviewers, detailing information like reviewer ID, movie title, genres, year, and rating. The analysis was performed on data stored in HDFS and executed on a Hadoop cluster.

**Features**

MapReduce Components: Uses a mapper, combiner, and reducer to process movie review data.

Hadoop Integration: The code runs on Hadoop, leveraging distributed computing to handle a large dataset efficiently.

Data Filtering: Movies are filtered based on release year, genre, and a minimum number of votes (at least 10 ratings).

Output Format: The result is presented as a TSV (tab-separated values) file listing the top-rated movie for each year.

**Technologies Used**

Python: Programming language used for creating the mapper, combiner, and reducer.

Hadoop MapReduce: Framework for distributed data processing.

HDFS: Storage system for the large dataset.


**MapReduce Workflow**

Mapper: Takes each line of the ratings file as input, splits it into individual components (reviewer ID, movie title, genres, year, rating), and emits key-value pairs of movie-year and rating.

Combiner: Aggregates the ratings for movies locally to reduce data sent across the network during the shuffle phase.

Reducer: Processes each movie-year key to calculate the average rating, filtering out movies with fewer than 10 ratings, and emits the top-rated movie(s) for each year.
