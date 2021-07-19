MENU_PROMPT = "select options 'a' for finding movies, 'b' for showing movies list, 'c' for adding movies:"

movies = []
def add_movies():
    Title = input("Movie title:")
    Director = input("Movie director name:")
    Year = input("Movie release date:")

    movies.append(
        {
        'title':Title,
        'director':Director,
        'year':Year
        }
    )

def find_movies():
    for movie in movies:
        user_input = input("movie title:")
        if user_input == movie['title']:
            print_movies(movie)


def print_movies(movie):
    for movie in movies:
        print(f" Movie Title: {movie['title']}")
        print(f"Movie director by:{movie['director']}")
        print(f"movie release year:{movie['year']}")

def show_movies():
    for movie in movies:
        print_movies(movie)



selection = input(MENU_PROMPT)
while selection != 'q':
    if selection == 'a':
        find_movies()
    elif selection == 'b':
        show_movies()
    elif selection == 'c':
        add_movies()
    else:
        print("No Results!!")

    print("searching for movies??")
    selection = input(MENU_PROMPT)


