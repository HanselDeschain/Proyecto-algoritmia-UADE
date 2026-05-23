

movies_name = [],
movies_ids = []
idx_years = []
idx_genres = []
years = []
genres = []
movies_rates = []

def search(array, idxToSearch):
    for i in range(len(array)):
        if array[i] == idxToSearch:
            return i
    return -1

def loadMovie(quantity):
    for i in range(quantity):
        loadMovieId()
        loadMovieName()
        loadMovieYear()
        loadMovieGenre()
        movieRate()

def loadMovieId():
    id = int(input("Ingresá un ID para la pelicula: "))
    idExists = search(movies_ids, id)

    if idExists == -1:
        movies_ids.append(id)

def loadMovieName():
    movie_name = input("ingresa el nombre: ")
    movieExists = search(movies_name, movies_name)

    if movieExists == -1:
        movie_name.append(movie_name)

def loadMovieYear():
    movie_year = int(input("ingresa el año de la pelicula: "))
    movieYearExists = search(years, movie_year)

    if movieYearExists == -1:
        years.append(movie_year)
        idx_years.append(len(years - 1))

def loadMovieGenre():
    movie_genre = input("Ingresá el género de la pelicula: ")
    genreExists = search(genres, movie_genre)

    if genreExists == -1:
        genres.append(movie_genre)
        idx_genres.append(len(genres - 1))

def movieRate():
    movie_rate = float(input("Ingresá la puntuación entre 0.0 y 5.0: "))
    while movie_rate <=0 or movie_rate >=5:
        print("la puntuación ingresada no es valida")
        movie_rate = float(input("Ingresá la puntuación entre 0.0 y 5.0: "))

    movies_rates.append(movie_rate)


def main():
    print("#--------- BIENVENIDO AL SISTEMA DE GESTIÓN DE PELICULAS ---------#")
    print("#----------------------- MENU DE OPCIONES -----------------------#")
    print("")
    print("1. Cargar Pelicula")
    print("")


    optionSelected = int(input("Seleccioná una opción para continuar:"))

    if optionSelected == 1:
        quantityOfMoviesToLoad = int(input("¿Cuantas peliculas querés subir? "))

        if quantityOfMoviesToLoad <= 0:
            print("No podés subir", quantityOfMoviesToLoad, "ingresá un número mayor a 0: ")
            quantityOfMoviesToLoad = int(input("¿Cuantas peliculas querés subir? "))
        loadMovie(quantityOfMoviesToLoad)
main()