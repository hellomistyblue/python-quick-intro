#Initialize a List of Movies
movie_collection = []

#Create a list named movie_collection where each element is a tuple containing the title, director, and release year.
movie_collection = [
    ("The Shawshank Redemption", "Frank Darabont", 1994),
    ("Inception", "Christopher Nolan", 2010),
    ("Spirited Away", "Hayao Miyazaki", 2001),
    ("The Matrix", "The Wachowskis", 1999),
    ("Forrest Gump", "Robert Zemeckis", 1994)
]

#Add Movies to the Collection
#Write a function add_movie(title, director, year) that adds a new movie tuple to the list.
def add_movie(title, director, release_year):
    new_movie = (title, director, release_year)
    movie_collection.append(new_movie)
    print(f"{title} by Director, {director} released in {release_year} added to collection.")


#Display All Movies
def display_movies():
    print("\n\nMovie Collection:")
    for title, director, release_year in movie_collection:
        print(f"Title: {title}, Director: {director}, Release Year: {release_year}")

#Search for Movies by Director
def search_by_director(director):
    movies_by_director = []
    for movie in movie_collection:
        title, movie_director, release_year = movie
        if movie_director.lower() == director.lower():
            movies_by_director.append(movie)
    return movies_by_director





display_movies()


add_movie("The Dark Knight", "Christopher Nolan", 2008)
add_movie("Interstellar", "Christopher Nolan", 2014)
add_movie("Pulp Fiction", "Quentin Tarantino", 1994)
add_movie("Parasite", "Bong Joon-ho", 2019)

display_movies()

movies_by_nolan = search_by_director("Christopher Nolan")
print("\nMovies by Christopher Nolan:")
for title, director, release_year in movies_by_nolan:
    print(f"Title: {title}, Release Year: {release_year}")