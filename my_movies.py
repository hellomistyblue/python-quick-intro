print("My output starts here")
# Initialize an empty list
favorite_movies = []

# Function to add movies to the list
def add_movie(movie):
    favorite_movies.append(movie)
    print(f"Movie {movie} added.")

# Function to remove a movie from the list
def remove_movie(movie):
    if movie in favorite_movies:
        favorite_movies.remove(movie)
        print(f"Movie {movie} removed.")
    else:
        print(f"Movie {movie} not found.")


# Function to display all favorite movies
def display_favorite_movies():
    print("Favorite Movie List:")
    for movie in favorite_movies:
        print(f"- {movie}")


# Function to count movies in list
def count_movies(movie_list):
    count = len(movie_list)
    print(count)
    return count



# Function to find a movie
def find_movie(movie):
    if movie in favorite_movies: 
        print(f"{movie} found.")
    else: 
        print(f"{movie} not found.")


# Function to clear the list
def clear_movies(movie_list):
    movie_list.clear()
    print(f"All movies in your list cleared. It's value is now: {movie_list}.")
    
add_movie('Inception')
add_movie('Godfather')
add_movie('Spaceballs')
add_movie('Titanic')

remove_movie('Titanic')
remove_movie('Jaws')

display_favorite_movies()

count_movies(favorite_movies)

find_movie('Spaceballs')
find_movie('Jaws')

clear_movies(favorite_movies)