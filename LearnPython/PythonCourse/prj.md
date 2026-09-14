# ==========================================
#       MOVIE RECOMMENDATION SYSTEM
# ==========================================

# List of movies
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


# ------------------------------------------
# FUNCTION 1: Display all movies
# ------------------------------------------

def show_movies():

    print("\n========== ALL MOVIES ==========")

    for movie in movies:
        print(
            movie["title"],
            "| Genre:", movie["genre"],
            "| Rating:", movie["rating"]
        )


# ------------------------------------------
# FUNCTION 2: Recommend movies
# ------------------------------------------

def recommend_movies():

    print("\n========== MOVIE RECOMMENDATION ==========")

    genre = input(
        "Enter your favorite genre: "
    ).lower()

    minimum_rating = float(
        input("Enter minimum rating (0 - 10): ")
    )

    found = False

    print("\nYour Recommendations:")
    print("---------------------")

    for movie in movies:

        if movie["genre"] == genre and movie["rating"] >= minimum_rating:

            print("🎬", movie["title"])
            print("   Genre:", movie["genre"])
            print("   Rating:", movie["rating"])
            print()

            found = True

    if found == False:
        print("No movies matched your preferences.")


# ------------------------------------------
# FUNCTION 3: Search for a movie
# ------------------------------------------

def search_movie():

    print("\n========== SEARCH MOVIE ==========")

    search = input("Enter movie title: ").lower()

    found = False

    for movie in movies:

        if search in movie["title"].lower():

            print("\nMovie Found!")
            print("Title:", movie["title"])
            print("Genre:", movie["genre"])
            print("Rating:", movie["rating"])

            found = True

    if found == False:
        print("Movie not found.")


# ------------------------------------------
# FUNCTION 4: Add a new movie
# ------------------------------------------

def add_movie():

    print("\n========== ADD MOVIE ==========")

    title = input("Enter movie title: ")
    genre = input("Enter movie genre: ").lower()
    rating = float(input("Enter movie rating: "))

    new_movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }

    movies.append(new_movie)

    print("\nMovie added successfully!")


# ------------------------------------------
# MAIN PROGRAM
# ------------------------------------------

while True:

    print("\n================================")
    print("     MOVIE RECOMMENDATION APP")
    print("================================")

    print("1. View all movies")
    print("2. Get recommendations")
    print("3. Search for a movie")
    print("4. Add a movie")
    print("5. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":

        show_movies()

    elif choice == "2":

        recommend_movies()

    elif choice == "3":

        search_movie()

    elif choice == "4":

        add_movie()

    elif choice == "5":

        print("\nThank you for using the Movie Recommendation System!")
        break

    else:

        print("\nInvalid choice. Please try again.")