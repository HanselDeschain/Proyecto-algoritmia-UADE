NOT_FOUND = -1


def search(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return NOT_FOUND


def create_movie_id(movies_ids):
    new_id = int(input("Ingresá el ID de la película (1000 a 9999): "))
    while new_id < 1000 or new_id > 9999 or search(movies_ids, new_id) != NOT_FOUND:
        if search(movies_ids, new_id) != NOT_FOUND:
            print("Ese ID ya existe.")
        else:
            print("El ID debe estar entre 1000 y 9999.")
        new_id = int(input("Ingresá el ID de la película (1000 a 9999): "))
    return new_id


def create_movie_name(movies_names):
    new_name = input("Ingresá el nombre de la película: ").strip().lower()
    while new_name == "" or search(movies_names, new_name) != NOT_FOUND:
        if search(movies_names, new_name) != NOT_FOUND:
            print("Esa película ya existe.")
        else:
            print("El nombre no puede estar vacío.")
        new_name = input("Ingresá el nombre de la película: ").strip().lower()
    return new_name


    while (newId < 1000 or newId > 9999) or search(movies_ids, newId) != NOT_FOUND:
        if search(movies_ids, newId) != NOT_FOUND:
            print("La pelicula con ese ID ya existe, intentá con otro")
        else:
            print("El ID debe ser un valor entre 1000 y 9999. ")
        print("")
        newId = int(input("Ingresá el ID de la pelicula: "))

    genres.append(new_genre)
    print("Género agregado correctamente.")


    while newName == "" or search(movies_name, newName) != NOT_FOUND:
        if search(movies_name, newName) != NOT_FOUND:
            print("La pelicula ", newName, " ya existe, intentá con otro")
        else:
            print("El nombre no puede estar vacio. ")
            print("")
        print("")
        newName = str(input("Ingresá el nombre de la pelicula: "))
    return newName

def createGenre(genres):
    newGenre = str(input("Ingresá el genéro de la pelicula: "))

    while newGenre == "" or search(genres, newGenre) != NOT_FOUND:
        if search(genres, newGenre) != NOT_FOUND:
            print("El genéro ", newGenre, " ya existe, intentá con otro")
        else:
            print("El genéro no puede estar vacio. ")
        print("")
        newGenre = str(input("Ingresá el genéro de la pelicula: "))

    years.append(new_year)
    print("Año agregado correctamente.")


    while (newYear < 1895 or newYear > 2026) or search(years, newYear) != NOT_FOUND:
        if search(years, newYear) != NOT_FOUND:
            print("El año ingresado ya existe, intentá con otro")
        else:
            print("El año no puede ser menor a 1895 o mayor a 2026.")
        print("")
        newYear = int(input("Ingresá el año de la pelicula: "))

def new_movie(movies_ids, movies_names, idx_genres, idx_years, movies_rates):
    movie_id = create_movie_id(movies_ids)
    movie_name = create_movie_name(movies_names)

def loadMovie(movies_ids, movies_name, idx_genres, idx_years, movies_rates, genres, years):
    """
    Función de carga de peliculas con los datos existentes
    """
    temp_movie_idx = getMovieId(movies_ids)

    if temp_movie_idx == "":
        return ## Retorna al menú para que cree el id y la pelicula
    
    movie_name = getMovieName(movies_name, temp_movie_idx)

def load_movie(movies_ids, movies_names, idx_genres, idx_years, movies_rates, genres, years):
    movie_index = get_movie_index(movies_ids)

    if movie_index == NOT_FOUND:
        return

    print("Película seleccionada:", movies_names[movie_index])

    genre_index = get_genre_index(genres)
    if genre_index == NOT_FOUND:
        return

    temp_movie_rate = getMovieRate()

    ## Si los datos no son "", se guardan los datos en las listas, si alguno devuelve ""(no existe), vuelve al menú
    ## Id y movie_name no son necesarios, ya que ya estan guardados, vamos a guardar idx_years, idx_genres y movie_rates
    idx_genres[temp_movie_idx] = temp_genre_idx
    idx_years[temp_movie_idx] = temp_year_idx
    movies_rates[temp_movie_idx] = temp_movie_rate

    print("¡Los datos de la pelicula ", movie_name, "fueron cargados correctamente!")

def getMovieId(movies_ids):
    """
    Retorna '' default si la pelicula no existe, si existe, devuelve el indice del id cargado
    """
    id = int(input("Ingresá un ID para la pelicula: "))
    idExists = search(movies_ids, id)
    result = ""
    if idExists == NOT_FOUND:
        printError(id)
    else:
        result = idExists
    return result

def getMovieName( movies_name, movie_idx):
    """
    Devuelve el nombre de la pelicula con el id recibido por argumento, si no existe el id, el programa falla antes
    """
    print("El nombre de la pelicula es:", movies_name[movie_idx])

    return movies_name[movie_idx]

    print("Datos cargados correctamente.")


def update_movie(movies_ids, movies_names, idx_genres, idx_years, movies_rates, genres, years):
    movie_index = get_movie_index(movies_ids)

    if movie_index == NOT_FOUND:
        return

    print("Película seleccionada:", movies_names[movie_index])
    print("1. Actualizar género")
    print("2. Actualizar año")
    print("3. Actualizar puntuación")
    print("4. Actualizar todo")
    print("0. Cancelar")

    option = int(input("Elegí una opción: "))

    if option == 1:
        genre_index = get_genre_index(genres)
        if genre_index != NOT_FOUND:
            idx_genres[movie_index] = genre_index
            print("Género actualizado.")

    elif option == 2:
        year_index = get_year_index(years)
        if year_index != NOT_FOUND:
            idx_years[movie_index] = year_index
            print("Año actualizado.")

    elif option == 3:
        movies_rates[movie_index] = get_movie_rate()
        print("Puntuación actualizada.")

    elif option == 4:
        genre_index = get_genre_index(genres)
        if genre_index == NOT_FOUND:
            return

        year_index = get_year_index(years)
        if year_index == NOT_FOUND:
            return

        movie_rate = get_movie_rate()

        idx_genres[movie_index] = genre_index
        idx_years[movie_index] = year_index
        movies_rates[movie_index] = movie_rate

        print("Película actualizada completamente.")

def showMovies(movies_ids, movies_name, idx_genres, idx_years, movies_rates, genres, years):
    """Funcion para mostrar el listado de peliculas"""
    if not len(movies_ids):
        print("")
        print("No hay peliculas cargadas")
    else:
        for id in range(len(movies_ids)):
            print("Pelicula nr°: ", id + 1)
            print("")
            print("ID: ", movies_ids[id])
            print("Nombre :", movies_name[id])

            # Verificar si ya fue cargado el género
            if idx_genres[id] == NOT_FOUND:
                print("Genéro:  Sin cargar")
            else:
                print("Genéro: ", genres[idx_genres[id]])

            # Verificar si ya fue cargado el año
            if idx_years[id] == NOT_FOUND:
                print("Año:  Sin cargar")
            else:
                print("Año: ", years[idx_years[id]])

            # Verificar si ya fue cargada la puntuación
            if movies_rates[id] == NOT_FOUND:
                print("Puntuacion:  Sin cargar")
            else:
                print("Puntuacion: ", movies_rates[id])

            print("")
        print("Todas las peliculas fueron listadas")

def showGenres(genres):
    if not len(genres):
        print("No hay generos para listar")

    print("Genéros totales:", len(genres))   
    for i in range(len(genres)):
        print(i, "-", genres[i])


def showYears(years):
    if not len(years):
        print("No hay años para listar")

    print("Años totales cargados:", len(years)) 
    for i in range(len(years)):
        print(i, "-", years[i])


def count_movies_by_genre(idx_genres, genres):
    if len(genres) == 0:
        print("No hay géneros cargados.")
        return

    if len(idx_genres) == 0:
        print("No hay películas creadas.")
        return

    print("\n--- CANTIDAD DE PELÍCULAS POR GÉNERO ---")
    for i in range(len(genres)):
        counter = 0
        for j in range(len(idx_genres)):
            if idx_genres[j] == i:
                counter += 1
        print(genres[i], ":", counter)

def count_movies_by_genre(idx_genres, genres):
    if len(genres) == 0:
        print("No hay géneros cargados.")
        return

    if len(idx_genres) == 0:
        print("No hay películas creadas.")
        return

    print("\n--- CANTIDAD DE PELÍCULAS POR GÉNERO ---")
    for i in range(len(genres)):
        counter = 0
        for j in range(len(idx_genres)):
            if idx_genres[j] == i:
                counter += 1
        print(genres[i], ":", counter)



def main():
    movies_ids = []
    movies_names = []

    idx_genres = []
    idx_years = []

    genres = []
    years = []

    movies_rates = []

    optionSelected = NOT_FOUND
    while optionSelected != 0:
        print("")
        print("#--------- BIENVENIDO AL SISTEMA DE GESTIÓN DE PELICULAS ---------#")
        print("#----------------------- MENU DE OPCIONES -----------------------#")
        print("")
        print("1. Crear pelicula")
        print("2. Cargar datos de la pelicula")
        print("3. Listar peliculas")
        print("")
        print("4. Crear genéro")
        print("5. Listar genéros")
        print("")
        print("6. Crear Año")
        print("7. Listar años")
        print("")
        print("8. Ordenar por nombre de pelicula")
        print("9. Ordenar por año de la pelicula")
        print("10. Ordenar por puntuacion")
        print("")
        print("11. Mostrar cantidad de peliculas por género")
        print("0. Finalizar programa")
        print("")

        optionSelected = int(input("Seleccioná una opción para continuar: "))

        if optionSelected == 1:
            loadMovie(movies_ids, movies_name, idx_genres, idx_years, movies_rates, genres, years)
        elif optionSelected == 2:
            newMovie(movies_ids, movies_name, idx_genres, idx_years, movies_rates)
        elif optionSelected == 3:
            showMovies(movies_ids, movies_name, idx_genres, idx_years, movies_rates, genres, years)
        elif optionSelected == 4:
            createGenre(genres)
        elif optionSelected == 5:
            showGenres(genres)
        elif optionSelected == 6:
            createYear(years)
        elif optionSelected == 7:
            showYears(years)
        elif optionSelected == 11:
            count_movies_by_genre(idx_genres, genres)
        elif optionSelected == 0:
            print("Saliendo...")

        else:
            print("Opción inválida.")


main()