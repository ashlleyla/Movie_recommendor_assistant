import ast
import pandas as pd

movies = pd.read_csv('tmdb_6000_movie_dataset.csv')
ratings = pd.read_csv('tmdb_6000_movie_ratings.csv')

def find_genres(text):
    genres = []
    try:
        data = ast.literal_eval(text)
        for item in data:
            genres.append(item['name'])
    except(ValueError, SyntaxError, TypeError):
        return []
    return genres
movies['genre_list'] = movies['genres'].apply(find_genres)
rating_summary = ratings.groupby('tmdbId')['rating'].agg(
    ['mean', 'count']
).reset_index()

rating_summary = rating_summary.rename(
    columns={
        'mean': 'average_rating',
        'count': 'number_of_ratings'
    }
)

movie_data = movies.merge(
    rating_summary,
    on='tmdbId',
    how='left'
)
movie_data['average_rating'] = movie_data['average_rating'].fillna(0)
movie_data['number_of_ratings'] = movie_data['number_of_ratings'].fillna(0)

genres = [
    'action',
    'adventure',
    'animation',
    'comedy',
    'crime',
    'drama',
    'family',
    'fantasy',
    'history',
    'horror',
    'music',
    'mystery',
    'romance',
    'science fiction',
    'thriller',
    'war'
]
rating_phrases = [
    'can you tell me the rating of',
    'tell me the rating for',
    'tell me the rating of',
    'what is the rating of',
    'what''s the rating of',
    'how is the movie',
    'what rating is',
    'rating of',
    'how is',
]
continue_program = 'yes'
while continue_program in ['yes', 'y']: 
    question = input(
        'Ask me about movies: '
    ).lower().strip()
    if question in ['quit', 'q', 'no', 'exit', 'stop']:
        break
    question = question.replace('movies', 'movie')
    movie_name = ''
    for phrase in rating_phrases: 
        if phrase in question:
            movie_name = question.replace(phrase, '')
            break
    if movie_name != '':
        movie_name = movie_name.replace('movie', '')
        movie_name = movie_name.replace('rated', '')
        movie_name = movie_name.replace('rating', '')
        movie_name = movie_name.replace('rating', '')
        movie_name = movie_name.replace('?', '')
        movie_name = movie_name.strip()
        exact_match = movie_data[
            movie_data['title'].str.lower() == movie_name
        ]
        if not exact_match.empty: 
            movie = exact_match.iloc[0]
            print(f"\nMovie: {movie['title']}")
            print(
                f"Average Rating: "
                f"{movie['average_rating']: .2f}"
            )
            print(
                f"Number of Ratings: "
                f"{int(movie['number_of_ratings'])}"
            )
        else:
            partial_matches = movie_data[
                movie_data['title'].str.lower().str.contains(
                    movie_name,
                    na=False
                )
            ]
            if partial_matches.empty:
                print('Movie not found.')
            elif len(partial_matches) == 1:
                movie = partial_matches.iloc[0]
                print(f"\nMovie: {movie['title']}")
                print(
                    f"Average Rating: "
                    f"{movie['average_rating']: .2f}"
                )
                print(
                    f"Number of Ratings: "
                    f"{int(movie['number_of_ratings'])}"
                )
            else:
                print('\nI found multiple possible movies: ')
                for number, (_, movie) in enumerate(
                    partial_matches.head(10).iterrows()
                ):
                    print(f"{number}, {movie['title']}")
    else: 
        selected_genre = ''
        for genre in genres:
            if genre in question:
                selected_genre = genre
                break
        if selected_genre == '':
            print('Sorry I could not find a movie title or a recognized genre.')
        else:
            recommendations = movie_data[
                movie_data['genre_list'].apply(
                    lambda movie_genres: any(
                        genre.lower() == selected_genre
                        for genre in movie_genres
                    )
                )
            ]
        
            recommendations = recommendations[
                recommendations['number_of_ratings'] >= 1000
            ]
            recommendations = recommendations.sort_values(
                by=[
                    'average_rating',
                    'number_of_ratings'
                ],
                ascending = [
                    False,
                    False
                ]
            )
            recommendations = recommendations.head(5)
            if recommendations.empty: 
                print(
                    f"No reliable {selected_genre} "
                    'recommendations were found.'
                )
            else:
                print(
                    f"\nTop {selected_genre.title()} Movies\n"
                )
                for number, (_, movie) in enumerate(
                recommendations.iterrows(),
                start=1
            ): 
                    print(
                        f"{number}. {movie['title']}"
                    )
                answer = input(
                    '\nWould you like to see the ratings? '
                    '(yes/no): '
                ).lower().strip()

                if answer in ['yes', 'y']:
                    print('\nMovie Ratings\n')
                    for number, (_, movie) in enumerate(
                        recommendations.iterrows(),
                        start=1
                    ):
                        print(f"{number}. {movie['title']}")
                        print(
                            f"Average Rating: "
                            f"{movie['average_rating']:.2f}"
                        )
                        print(
                            f"Number of Ratings: "
                            f"{int(movie['number_of_ratings'])}"
                        )
                        print()
                continue_program = input(
                    '\nWould you like to ask about another movie or genre? (yes/no): '
                ).lower().strip()
print('Bye Bye!')