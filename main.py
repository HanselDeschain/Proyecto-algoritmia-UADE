NOT_FOUND = -1

def printError(value):
    """Acepta un valor como argumento y lo usa para imprimir un mensaje de error genérico"""
    print(value, "No existe, primero crealo desde el menú")
    print("")


def search(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return NOT_FOUND

def newMovie(movies_ids, movies_name, idx_genres, idx_years, movies_rates):
    """
    Función de CREACIÓN de movie_id y movie_name
    """
    movieId = createMovieId(movies_ids)
    movieName = createMovieName(movies_name)

    movies_ids.append(movieId)
    movies_name.append(movieName)
    ## Parte final de la creación, reservamos el espacio, por ahora en blanco, para luego reemplazar el lugar con el dato final sobre esa pelicula, manteniendo las listas paralelas alineadas
    idx_genres.append(NOT_FOUND)
    idx_years.append(NOT_FOUND)
    movies_rates.append(NOT_FOUND)

    print("¡Pelicula creada exitosamente!")
    return

def createMovieId(movies_ids):
    """
    Id de la pelicula, debe ser un número entre 1000 y 9999, además no debe de existir en el array de id's
    """
    newId = int(input("Ingresá el ID de la pelicula: "))

    while (newId < 1000 or newId > 9999) or search(movies_ids, newId) != NOT_FOUND:
        if search(movies_ids, newId) != NOT_FOUND:
            print("La pelicula con ese ID ya existe, intentá con otro")
        else:
            print("El ID debe ser un valor entre 1000 y 9999. ")
        print("")
        newId = int(input("Ingresá el ID de la pelicula: "))

    return newId

def createMovieName(movies_name):
    """Nombre de la pelicula ingresado para el usuario, la pelicula no puede existir o estar vacia"""
    newName = str(input("Ingresá el nombre de la pelicula: "))

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

    genres.append(newGenre)
    print("¡Genéro agregado correctamente!")

def createYear(years):
    newYear = int(input("Ingresá el año de la pelicula: "))

    while (newYear < 1895 or newYear > 2026) or search(years, newYear) != NOT_FOUND:
        if search(years, newYear) != NOT_FOUND:
            print("El año ingresado ya existe, intentá con otro")
        else:
            print("El año no puede ser menor a 1895 o mayor a 2026.")
        print("")
        newYear = int(input("Ingresá el año de la pelicula: "))

    years.append(newYear)
    print("¡Año agregado correctamente!")

def loadMovie(movies_ids, movies_name, idx_genres, idx_years, movies_rates, genres, years):
    """
    Función de carga de peliculas con los datos existentes
    """
    temp_movie_idx = getMovieId(movies_ids)

    if temp_movie_idx == "":
        return ## Retorna al menú para que cree el id y la pelicula
    
    movie_name = getMovieName(movies_name, temp_movie_idx)

    temp_year_idx = getMovieYear(years)

    if temp_year_idx == "":
        return

    temp_genre_idx = getMovieGenre(genres)
    if temp_genre_idx == "":
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

def getMovieName(movies_name, movie_idx):
    """
    Devuelve el nombre de la pelicula con el id recibido por argumento, si no existe el id, el programa falla antes
    """
    print("El nombre de la pelicula es:", movies_name[movie_idx])

    return movies_name[movie_idx]

def getMovieYear(years):
    year = int(input("Ingresá el año de la pelicula: "))
    yearIdx = search(years, year)
    result = ""

    if yearIdx == NOT_FOUND:
        printError(year)
    else:
        result = yearIdx

    return result

def getMovieGenre(genres):
    movieGenre = input("Ingresá el género de la pelicula: ")
    genreIdx = search(genres, movieGenre)
    result = ""

    if genreIdx == NOT_FOUND:
        printError(movieGenre)
    else:
        result = genreIdx
    return result

def getMovieRate():
    movieRate = float(input("Ingresá la puntuación entre 1 y 5: "))

    while movieRate < 1 or movieRate > 5:
        print("la puntuación ingresada no es valida, debe ser entre 1 a 5")
        print("")
        movieRate = float(input("Ingresá la puntuación entre 1 y 5: "))

    return movieRate

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
        return

    print("Genéros totales:", len(genres))   
    for i in range(len(genres)):
        print("Genéro: ", genres[i])

def showYears(years):
    if not len(years):
        print("No hay años para listar")
        return

    print("Años totales cargados:", len(years)) 
    for i in range(len(years)):
        print("Año: ", years[i])

def countMoviesByGenre(idx_genres, genres):
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

def calculateAverageReview(reviews):
    if not len(reviews):
        print("No hay puntuaciones cargadas")
        return
    total = 0
    withReview = 0

    for i in range(len(reviews)):
        if reviews[i] != NOT_FOUND:
            total += reviews[i]
            withReview += 1

    if withReview == 0:
        print("No hay puntuaciones cargadas")
        return
    
    print("La puntuación promedio es: ", total / withReview)

def sortByName(movies_ids, movies_name, idx_genres, idx_years, movies_rates):
    """Ordena todas las listas paralelas alfabéticamente por nombre de película (bubble sort)"""
    if not len(movies_name):
        print("No hay películas para ordenar.")
        return

    n = len(movies_name)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if movies_name[j] > movies_name[j + 1]:
                # Se intercambian todas las listas a la vez para mantener el paralelismo
                movies_name[j], movies_name[j + 1] = movies_name[j + 1], movies_name[j]
                movies_ids[j], movies_ids[j + 1] = movies_ids[j + 1], movies_ids[j]
                idx_genres[j], idx_genres[j + 1] = idx_genres[j + 1], idx_genres[j]
                idx_years[j], idx_years[j + 1] = idx_years[j + 1], idx_years[j]
                movies_rates[j], movies_rates[j + 1] = movies_rates[j + 1], movies_rates[j]

    print("¡Películas ordenadas por nombre correctamente!")


def sortByYear(movies_ids, movies_name, idx_genres, idx_years, movies_rates, years):
    """Ordena todas las listas paralelas por año de la película de menor a mayor (bubble sort).
    Si alguna película no tiene año cargado (NOT_FOUND), se saltea el swap y se la deja donde está."""
    if not len(movies_name):
        print("No hay películas para ordenar.")
        return

    n = len(idx_years)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            # Si alguna de las dos no tiene año cargado, no se comparan
            if idx_years[j] == NOT_FOUND or idx_years[j + 1] == NOT_FOUND:
                continue

            if years[idx_years[j]] > years[idx_years[j + 1]]:
                # Se intercambian todas las listas a la vez para mantener el paralelismo
                movies_name[j], movies_name[j + 1] = movies_name[j + 1], movies_name[j]
                movies_ids[j], movies_ids[j + 1] = movies_ids[j + 1], movies_ids[j]
                idx_genres[j], idx_genres[j + 1] = idx_genres[j + 1], idx_genres[j]
                idx_years[j], idx_years[j + 1] = idx_years[j + 1], idx_years[j]
                movies_rates[j], movies_rates[j + 1] = movies_rates[j + 1], movies_rates[j]

    print("¡Películas ordenadas por año correctamente!")


def sortByRate(movies_ids, movies_name, idx_genres, idx_years, movies_rates):
    """Ordena todas las listas paralelas por puntuación de mayor a menor (bubble sort).
    Si alguna película no tiene puntuación cargada (NOT_FOUND), se saltea el swap y se la deja donde está."""
    if not len(movies_name):
        print("No hay películas para ordenar.")
        return

    n = len(movies_rates)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            # Si alguna de las dos no tiene puntuación cargada, no se comparan
            if movies_rates[j] == NOT_FOUND or movies_rates[j + 1] == NOT_FOUND:
                continue

            if movies_rates[j] < movies_rates[j + 1]:
                # Se intercambian todas las listas a la vez para mantener el paralelismo
                movies_name[j], movies_name[j + 1] = movies_name[j + 1], movies_name[j]
                movies_ids[j], movies_ids[j + 1] = movies_ids[j + 1], movies_ids[j]
                idx_genres[j], idx_genres[j + 1] = idx_genres[j + 1], idx_genres[j]
                idx_years[j], idx_years[j + 1] = idx_years[j + 1], idx_years[j]
                movies_rates[j], movies_rates[j + 1] = movies_rates[j + 1], movies_rates[j]

    print("¡Películas ordenadas por puntuación correctamente!")


def main():
    movies_name = []
    movies_ids = []

    idx_years = []
    years = []

    idx_genres = []
    genres = []

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
        print("12. Mostrar promedio de puntuación")
        print("0. Finalizar programa")
        print("")

        optionSelected = int(input("Seleccioná una opción para continuar: "))

        if optionSelected == 1:
            newMovie(movies_ids, movies_name, idx_genres, idx_years, movies_rates)
        elif optionSelected == 2:
            loadMovie(movies_ids, movies_name, idx_genres, idx_years, movies_rates, genres, years)
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
        elif optionSelected == 8:
            sortByName(movies_ids, movies_name, idx_genres, idx_years, movies_rates)
        elif optionSelected == 9:
            sortByYear(movies_ids, movies_name, idx_genres, idx_years, movies_rates, years)
        elif optionSelected == 10:
            sortByRate(movies_ids, movies_name, idx_genres, idx_years, movies_rates)
        elif optionSelected == 11:
            countMoviesByGenre(idx_genres, genres)
        elif optionSelected == 12:
            calculateAverageReview(movies_rates)
        elif optionSelected == 0:
            print("Saliendo...")
        else:
            print("Opcion inválida.")

main()
