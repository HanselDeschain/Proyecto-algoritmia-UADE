movies_ids = []
movies_names = []
movies_genres = []
movies_years = []
movies_rates = []


def search(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1


def ask_movie_id():
    movie_id = int(input("Ingresá el ID de la película: "))
    while movie_id < 1000 or movie_id > 9999:
        print("Error: el ID debe estar entre 1000 y 9999.")
        movie_id = int(input("Ingresá el ID de la película: "))
    return movie_id


def ask_movie_name():
    movie_name = input("Ingresá el nombre de la película: ")
    while movie_name == "":
        print("Error: el nombre no puede estar vacío.")
        movie_name = input("Ingresá el nombre de la película: ")
    return movie_name


def ask_movie_genre():
    movie_genre = input("Ingresá el género de la película: ")
    while movie_genre == "":
        print("Error: el género no puede estar vacío.")
        movie_genre = input("Ingresá el género de la película: ")
    return movie_genre


def ask_movie_year():
    movie_year = int(input("Ingresá el año de la película: "))
    while movie_year < 1888 or movie_year > 2100:
        print("Error: ingresá un año válido.")
        movie_year = int(input("Ingresá el año de la película: "))
    return movie_year


def ask_movie_rate():
    movie_rate = float(input("Ingresá la puntuación de la película (0 a 5): "))
    while movie_rate < 0 or movie_rate > 5:
        print("Error: la puntuación debe estar entre 0 y 5.")
        movie_rate = float(input("Ingresá la puntuación de la película (0 a 5): "))
    return movie_rate


def create_movie():
    movie_id = ask_movie_id()

    if search(movies_ids, movie_id) != -1:
        print("Error: ya existe una película con ese ID.")
        return

    movie_name = ask_movie_name()

    if search(movies_names, movie_name) != -1:
        print("Error: ya existe una película con ese nombre.")
        return

    movie_genre = ask_movie_genre()
    movie_year = ask_movie_year()
    movie_rate = ask_movie_rate()

    movies_ids.append(movie_id)
    movies_names.append(movie_name)
    movies_genres.append(movie_genre)
    movies_years.append(movie_year)
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
    option = -1

    while option != 0:
        print("\n#--------- SISTEMA DE GESTIÓN DE PELÍCULAS ---------#")
        print("1. Cargar película")
        print("2. Mostrar películas")
        print("0. Salir")

        option = int(input("Seleccioná una opción: "))

        if option == 1:
            create_movie()
        elif option == 2:
            show_movies()
        elif option == 0:
            print("Programa finalizado.")
        else:
            print("Opción inválida.")


main()
