movies_name = ["Patrón"],
movies_ids = [1111]

idx_years = []
years = []

idx_genres = []
genres_id = []
genres = []

movies_rates = []



def search(array, idxToSearch):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return NOT_FOUND

def newMovie():
    """
    Función de CREACIÓN de movie_id y movie_name
    """

    ## Parte final de la creación, reservamos el espacio, por ahora en blanco, para luego reemplazar el lugar con el dato final sobre esa pelicula, manteniendo las listas paralelas alineadas
    idx_genres.append("")
    idx_years.append("")
    movies_rates.append("")
    return 

def loadMovie():
    """
    Función de carga de peliculas con los datos existentes
    """
    temp_movie_id = getMovieId()

    if temp_movie_id == "":
        return ## Retorna al menú para que cree el id y la pelicula
    
    movie_name = getMovieName(temp_movie_id)

    temp_year_idx = getMovieYear()

    if search(movies_names, movie_name) != -1:
        print("Error: ya existe una película con ese nombre.")
        return

    ## Si los datos no son "", se guardan los datos en las listas, si alguno devuelve ""(no existe), vuelve al menú
    ## Id y movie_name no son necesarios, ya que ya estan guardados, vamos a guardar idx_years, idx_genres y movie_rates
    idx_years[temp_movie_id] = temp_year_idx

def getMovieId():
    """
    Retorna '' default si la pelicula no existe, si existe, devuelve el indice del id cargado
    """
    id = int(input("Ingresá un ID para la pelicula: "))
    idExists = search(movies_ids, id)
    resultado = ""
    if idExists == -1:
        print("El ID ingresado no existe. Primero crealo desde el menú")
    else:
        resultado = idExists
    return resultado

def getMovieName(movie_id):
    """
    Devuelve el nombre de la pelicula con el id recibido por argumento, si no existe el id, el programa falla antes
    """
    movieIdIndex = search(movies_ids, movie_id)
    print("El nombre de la pelicula es:", movies_name[movieIdIndex])

    return movies_name[movieIdIndex]

def getMovieYear():
     year = int(input("Ingresá el año de la pelicula: "))
     year_idx = search(years, year)
     resultado = ""

     if year_idx == -1:
        print("El año ingresado no existe. Primero crealo desde el menú")
     else:
        resultado = year_idx

     return resultado

def loadMovieGenre():
    movie_genre = input("Ingresá el género de la pelicula: ")
    genreExists = search(genres, movie_genre)
    print(genreExists)
    if genreExists == -1:
        genres.append(movie_genre)
        idx_genres.append(len(genres - 1))

def movieRate():
    movie_rate = float(input("Ingresá la puntuación entre 0.0 y 5.0: "))
    while movie_rate <=0 or movie_rate >=5:
        print("la puntuación ingresada no es valida")
        movie_rate = float(input("Ingresá la puntuación entre 0.0 y 5.0: "))

    movies_rates.append(movie_rate)

    print("Película cargada correctamente.")


def show_movies():
    if len(movies_ids) == 0:
        print("No hay películas cargadas.")
        return

    print("\n--- LISTADO DE PELÍCULAS ---")
    for i in range(len(movies_ids)):
        print("ID:", movies_ids[i])
        print("Nombre:", movies_names[i])
        print("Género:", movies_genres[i])
        print("Año:", movies_years[i])
        print("Puntuación:", movies_rates[i])
        print("----------------------------")


def main():
    optionSelected = 10000
    while optionSelected != 0:
        print("")
        print("#--------- BIENVENIDO AL SISTEMA DE GESTIÓN DE PELICULAS ---------#")
        print("#----------------------- MENU DE OPCIONES -----------------------#")
        print("")
        print("1. Cargar Pelicula")
        print("2. Crear pelicula")
        print("0. Finalizar programa")
        print("")

        optionSelected = int(input("Seleccioná una opción para continuar: "))

        if optionSelected == 1:
            loadMovie()
main()