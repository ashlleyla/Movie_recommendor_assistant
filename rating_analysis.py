import pandas as pd
# datasets
movies = pd.read_csv("tmdb_6000_movie_dataset.csv")
ratings = pd.read_csv("tmdb_6000_movie_ratings.csv")
# merging movie titles with user ratings
combined = ratings.merge(
    movies[['tmdbId', 'title', 'genres']],
    on='tmdbId',
    how='inner'
)
# calculating average rating and number of ratings for each movie
movie_summary = combined.groupby('title')['rating'].agg(
    ['mean', 'count']
).reset_index()

# renaming columns
movie_summary = movie_summary.rename(
    columns = {
        'mean': 'average_rating',
        'count': 'number_of_ratings'
    }
)

# round average ratings
movie_summary['average_rating'] = (
    movie_summary['average_rating'].round(2)
)

# printing all basic dataset information
print('RATINGS DATASET SUMMARY')
print('-----------------------')
print(f"Total ratings: {len(ratings)}")
print(f"Total users: {ratings['userId'].nunique()}")
print(f"Total rated movies: {ratings['tmdbId'].nunique()}")

# Top 10 most-rated movies
most_rated = movie_summary.sort_values(
    by='number_of_ratings',
    ascending=False
).head(10)

print('\nTOP !) MOST-RATED MOVIES')
print('--------------------------')

for number, (_, movie) in enumerate(
    most_rated.iterrows(),
    start=1
):
    print(
        f"{number}. {movie['title']} | "
        f"Average Rating: {movie['average_rating']: .2f}"
        f"Number of Ratings: {int(movie['number_of_ratings'])}"
    )

# keep movies with at least 1,000 ratings
reliable_movies = movie_summary[
    movie_summary["number_of_ratings"] >= 1000
]

# show the 10 highest-rated reliable movies
highest_rated = reliable_movies.sort_values(
    by=[
        "average_rating",
        "number_of_ratings"
    ],
    ascending=[
        False,
        False
    ]
).head(10)

print("\nTOP 10 HIGHEST-RATED MOVIES")
print("-----------------------------")
print("Only movies with at least 1,000 ratings are included.")
for number, (_, movie) in enumerate(
    highest_rated.iterrows(),
    start=1
):
    print(
        f"{number}. {movie['title']} | "
        f"Average Rating: {movie['average_rating']:.2f} | "
        f"Number of Ratings: {int(movie['number_of_ratings'])}"
    )

# overall average rating
overall_average = ratings["rating"].mean()

print("\nOVERALL AVERAGE USER RATING")
print("---------------------------")
print(f"{overall_average:.2f}")

rating_distribution = ratings["rating"].value_counts().sort_index()

print("\nRATING DISTRIBUTION")
print("-------------------")

for rating, count in rating_distribution.items():
    print(f"Rating {rating}: {count} ratings")