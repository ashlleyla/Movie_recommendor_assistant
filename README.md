# Movie Recommendation and Rating
## Overview
The Movie Recommendation and Rating Assistant is a Python application that recommends movies based on genre and provides rating information using datasets from Kaggle.
This project demonstrates data science workflow by loading, cleaning, analyzing and merging movie data before allowing users to interact with the dataset through the command-line interface.

## Features
- Recommend movies by genre
- Displays average movie ratings
- Displays the number of user ratings
- Searches the rating of a specific movie
- Recognize multiple user question formats
- Handle invalid movie titles and genres
- Allow multiple searches without restarting the program
- Allow exit of the program at any time

## Technologies Used
- Python
- Pandas
- AST
- CSV Datasets
- VS Code

## Dataset
This project uses two datasets from Kaggle:
- TMDB 6000 Movie Dataset
- TMDB 6000 Movie Ratings Dataset

These datasets contain information such as:
- Movie Titles
- Genres
- Keywords
- Overviews
- Popularity
- User ratings
- Number of ratings

## How it Works
### Step 1: Load the Data
Both CSV datasets are loaded into Pandas DataFrames.
### Step 2: Clean the Data
The program:
- Removes unnecessary columns
- Removes missing values
- Converts genre strings into Python lists
- Merges the movie dataset with the ratings dataset
### Step 3: Analyze the Data
`rating_analysis.py` performs exploratory data analysis by displaying:
- Total ratings
- Total users
- Total rated movies
- Top 10 most-rated movies
- Top 10 highest-rated movies
- Overall average rating
- Rating distribution
### Step 4: Recommend Movies
Users can ask for recommendations by genre.
Example:
```
Recommend horror movies
```
The assistant returns the top-rated movies within that genre.
### Step 5: View Ratings
After displaying recommendations, users can choose to view:
- Average Rating
- Number of Ratings
### Step 6: Search Individual Movies
Users can ask questions such as:
```
What is the rating of Avatar?
```
or
```
Tell me the rating for Titanic.
```
The assistant displays:
- Movie title
- Average rating
- Number of ratings
## Example Questions
### Genre Recommendation
```
Recommend horror movies
```
```
Recommend comedy movies
```
```
Recommend action movies
```

### Rating Lookup
```
What is the rating of Avatar?
```
```
Tell me the rating of Parasite.
```
```
Rating of Titanic
```
## Screenshots
### Genre Recommendation and Rating
![Genre Recommendation and Rating](screenshots/recommendation_and_rating.png)
### Movie Ratings
![Movie Ratings](screenshots/successful_rating.png)
## Genre Recommendation
![Genre Recommendation](screenshots/successful_recommendation.png)
### Invalid Inputs
![Invalid Inputs](screenshots/invalid_inputs.png)
### Rating Analysis
![Rating Analysis](screenshots/rating_analysis.png)

## Skills Demonstrated
- Data Cleaning
- Data Wrangling
- Exploratory Data Analysis (EDA)
- Data Merging
- Data Aggregation
- User Input Validation
- Python Programming
- Pandas
- Functions
- Loops
- Conditional Statements
- Error Handling
- Working with Real-World Datasets

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/movie_recommender.git
```

Navigate to the project:

```bash
cd movie_recommender
```

Install the required package:

```bash
pip install -r requirements.txt
```

Run the recommender:

```bash
python3 movie_recommender.py
```

Run the rating analysis:

```bash
python3 rating_analysis.py
```
## Author
Seoyeun La
Created as a portfolio project to demonstrate Python programming, data analysis, and recommendation system development for Data Science internship opportunities.
