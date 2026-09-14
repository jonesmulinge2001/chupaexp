# Movie recommendation system
# List of movies
# List of Movies and each movie is an objct
movies = [
    {
        "title": "Avengers: Endgame",
        "genre": "action",
        "rating": 8.4
    },
    {
        "title": "The Dark Knight",
        "genre": "action",
        "rating": 9.0
    },
    {
        "title": "Titanic",
        "genre": "romance",
        "rating": 7.9
    },
    {
        "title": "The Notebook",
        "genre": "romance",
        "rating": 7.8
    },
    {
        "title": "The Conjuring",
        "genre": "horror",
        "rating": 7.5
    },
    {
        "title": "Insidious",
        "genre": "horror",
        "rating": 6.8
    },
    {
        "title": "Interstellar",
        "genre": "science fiction",
        "rating": 8.7
    },
    {
        "title": "Inception",
        "genre": "science fiction",
        "rating": 8.8
    }
]

# function to display all the mivies
def displayMovies():
    print("--------All the Movies--------------")
    for movie in movies:
        print(f"{movie['title']}, {movie['genre'], {movie['rating']}}")
# displayMovies()

# recommend movie to a user
def recommend_movie():
    print("===Recommend Movie====")
    genre = input("Enter your favorite genre: ").lower().strip()
    minimum_rating = float(input("Enter the minimum movie rating: "))
    found = False
    for movie in movies:
        if movie['genre'] == genre and movie['rating'] >= minimum_rating:
            print("===Your Recommendations===")
            print(f"Title: {movie['title']}")
            print(f"Genre: {movie['genre']}")
            print(f"Rating: {movie['rating']}")
            print("\n")
            found = True
    
    if found == False:
        print("No movie to recommend to you")

# recommend_movie()

# serach for a movie
def search_movie():
    print("===Search for a movie===")
    search = input("Search for a movie: ").lower().strip()
    found = False
    for movie in movies:
        if search in movie['title']:
            print("===Movie found===")
            print(f"Title: {movie['title']}")
            print(f"Genre: {movie['genre']}")
            print(f"Rating: {movie['rating']} ")
            found = True
    
    if found == False:
        print("No movie that matches your search! Try adjusting your keywords")


# add a movie to the existing movies
def addMovie():
    print("=== Add a movie ===")
    title = input("Enter the title of the movie: ").lower().strip()
    genre = input(f"Enter the genre for {title}: ")
    rating = input(f"Enter the rating of {title}: ")

    # create a dictionary of the new movie
    new_movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }

    movies.append(new_movie)


# Entry Point of the System
while True:
    print('=== Welcome to Movie Recommendation System===')
    print("\n1. Show Available movies")
    print("\n2. Get a movie recommendation")
    print("\n3. Search a movie")
    print("\n4. Add movie")
    print("\n5. Exit")

    choice = input("Select an option: ").strip()
    if choice == '1':
        displayMovies()
    elif choice == '2':
        recommend_movie()
    elif choice == '3':
        search_movie()
    elif choice == '4':
        addMovie()
    elif choice == '5':
        exit()
    else:
        print('Invalid choice')
        exit()