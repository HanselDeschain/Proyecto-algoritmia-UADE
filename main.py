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


def create_genre(genres):
    new_genre = input("Ingresá un género nuevo: ").strip().lower()
    while new_genre == "" or search(genres, new_genre) != NOT_FOUND:
        if search(genres, new_genre) != NOT_FOUND:
            print("Ese género ya existe.")
        else:
            print("El género no puede estar vacío.")
        new_genre = input("Ingresá un género nuevo: ").strip().lower()

    genres.append(new_genre)
    print("Género agregado correctamente.")


def create_year(years):
    new_year = int(input("Ingresá un año nuevo: "))
    while new_year < 1895 or new_year > 2026 or search(years, new_year) != NOT_FOUND:
        if search(years, new_year) != NOT_FOUND:
            print("Ese año ya existe.")
        else:
            print("El año debe estar entre 1895 y 2026.")
        new_year = int(input("Ingresá un año nuevo: "))

    years.append(new_year)
    print("Año agregado correctamente.")


def get_movie_index(movies_ids):
    movie_id = int(input("Ingresá el ID de la película: "))
    idx = search(movies_ids, movie_id)
    if idx == NOT_FOUND:
        print("No existe una película con ese ID.")
    return idx


def get_genre_index(genres):
    genre_name = input("Ingresá el género de la película: ").strip().lower()
    idx = search(genres, genre_name)
    if idx == NOT_FOUND:
        print("Ese género no existe. Primero crealo desde el menú.")
    return idx


def get_year_index(years):
    year_value = int(input("Ingresá el año de la película: "))
    idx = search(years, year_value)
    if idx == NOT_FOUND:
        print("Ese año no existe. Primero crealo desde el menú.")
    return idx


def get_movie_rate():
    rate = float(input("Ingresá la puntuación de la película (1 a 5): "))
    while rate < 1 or rate > 5:
        print("La puntuación debe estar entre 1 y 5.")
        rate = float(input("Ingresá la puntuación de la película (1 a 5): "))
    return rate


def new_movie(movies_ids, movies_names, idx_genres, idx_years, movies_rates):
    movie_id = create_movie_id(movies_ids)
    movie_name = create_movie_name(movies_names)

    movies_ids.append(movie_id)
    movies_names.append(movie_name)

    # se reserva espacio para completar luego
    idx_genres.append(NOT_FOUND)
    idx_years.append(NOT_FOUND)
    movies_rates.append(NOT_FOUND)

    print("Película creada correctamente.")


def load_movie(movies_ids, movies_names, idx_genres, idx_years, movies_rates, genres, years):
    movie_index = get_movie_index(movies_ids)

    if movie_index == NOT_FOUND:
        return

    print("Película seleccionada:", movies_names[movie_index])

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

    elif option == 0:
        print("Actualización cancelada.")
    else:
        print("Opción inválida.")


def show_movies(movies_ids, movies_names, idx_genres, idx_years, movies_rates, genres, years):
    if len(movies_ids) == 0:
        print("No hay películas cargadas.")
        return

    print("\n--- LISTADO DE PELÍCULAS ---")
    for i in range(len(movies_ids)):
        print("Registro:", i + 1)
        print("ID:", movies_ids[i])
        print("Nombre:", movies_names[i])

        if idx_genres[i] == NOT_FOUND:
            print("Género: Sin cargar")
        else:
            print("Género:", genres[idx_genres[i]])

        if idx_years[i] == NOT_FOUND:
            print("Año: Sin cargar")
        else:
            print("Año:", years[idx_years[i]])

        if movies_rates[i] == NOT_FOUND:
            print("Puntuación: Sin cargar")
        else:
            print("Puntuación:", movies_rates[i])

        print("----------------------------")


def show_genres(genres):
    if len(genres) == 0:
        print("No hay géneros cargados.")
        return

    print("\n--- GÉNEROS ---")
    for i in range(len(genres)):
        print(i, "-", genres[i])


def show_years(years):
    if len(years) == 0:
        print("No hay años cargados.")
        return

    print("\n--- AÑOS ---")
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


def main():
    movies_ids = []
    movies_names = []

    idx_genres = []
    idx_years = []

    genres = []
    years = []

    movies_rates = []

    option = -1

    while option != 0:
        print("\n#--------- SISTEMA DE GESTIÓN DE PELÍCULAS ---------#")
        print("1. Crear película")
        print("2. Cargar datos de película")
        print("3. Actualizar película")
        print("4. Listar películas")
        print("5. Crear género")
        print("6. Listar géneros")
        print("7. Crear año")
        print("8. Listar años")
        print("9. Mostrar cantidad de películas por género")
        print("0. Salir")

        option = int(input("Seleccioná una opción: "))

        if option == 1:
            new_movie(
                movies_ids,
                movies_names,
                idx_genres,
                idx_years,
                movies_rates,
            )

        elif option == 2:
            load_movie(
                movies_ids,
                movies_names,
                idx_genres,
                idx_years,
                movies_rates,
                genres,
                years,
            )

        elif option == 3:
            update_movie(
                movies_ids,
                movies_names,
                idx_genres,
                idx_years,
                movies_rates,
                genres,
                years,
            )

        elif option == 4:
            show_movies(
                movies_ids,
                movies_names,
                idx_genres,
                idx_years,
                movies_rates,
                genres,
                years,
            )

        elif option == 5:
            create_genre(genres)

        elif option == 6:
            show_genres(genres)

        elif option == 7:
            create_year(years)

        elif option == 8:
            show_years(years)

        elif option == 9:
            count_movies_by_genre(idx_genres, genres)

        elif option == 0:
            print("Saliendo...")

        else:
            print("Opción inválida.")


main()