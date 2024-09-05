class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.detalle = (titulo, autor)  # Tupla inmutable para título y autor
        self.categoria = categoria
        self.isbn = isbn

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros prestados

class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario ISBN -> Libro
        self.usuarios = {}  # Diccionario ID -> Usuario
        self.ids_usuarios = set()  # Conjunto para asegurar IDs únicos de usuarios
    
    def agregar_libro(self):
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        categoria = input("Ingrese la categoría del libro: ")
        isbn = input("Ingrese el ISBN del libro: ")
        
        if isbn in self.libros_disponibles:
            print(f"El libro con ISBN {isbn} ya existe en la biblioteca.")
        else:
            nuevo_libro = Libro(titulo, autor, categoria, isbn)
            self.libros_disponibles[isbn] = nuevo_libro
            print(f"Libro '{titulo}' agregado a la biblioteca.")
    
    def quitar_libro(self):
        isbn = input("Ingrese el ISBN del libro a eliminar: ")
        if isbn in self.libros_disponibles:
            libro = self.libros_disponibles.pop(isbn)
            print(f"Libro '{libro.detalle[0]}' eliminado de la biblioteca.")
        else:
            print(f"No se encontró un libro con ISBN {isbn}.")
    
    def registrar_usuario(self):
        nombre = input("Ingrese el nombre del usuario: ")
        id_usuario = input("Ingrese el ID del usuario: ")
        
        if id_usuario in self.ids_usuarios:
            print(f"El usuario con ID {id_usuario} ya está registrado.")
        else:
            nuevo_usuario = Usuario(nombre, id_usuario)
            self.usuarios[id_usuario] = nuevo_usuario
            self.ids_usuarios.add(id_usuario)
            print(f"Usuario '{nombre}' registrado con éxito.")
    
    def dar_de_baja_usuario(self):
        id_usuario = input("Ingrese el ID del usuario a dar de baja: ")
        
        if id_usuario in self.usuarios:
            usuario = self.usuarios.pop(id_usuario)
            self.ids_usuarios.remove(id_usuario)
            print(f"Usuario '{usuario.nombre}' dado de baja.")
        else:
            print(f"No se encontró un usuario con ID {id_usuario}.")
    
    def prestar_libro(self):
        id_usuario = input("Ingrese el ID del usuario: ")
        isbn = input("Ingrese el ISBN del libro a prestar: ")
        
        if id_usuario not in self.usuarios:
            print(f"No se encontró un usuario con ID {id_usuario}.")
            return
        
        if isbn not in self.libros_disponibles:
            print(f"El libro con ISBN {isbn} no está disponible.")
            return
        
        usuario = self.usuarios[id_usuario]
        libro = self.libros_disponibles.pop(isbn)
        usuario.libros_prestados.append(libro)
        print(f"Libro '{libro.detalle[0]}' prestado a '{usuario.nombre}'.")
    
    def devolver_libro(self):
        id_usuario = input("Ingrese el ID del usuario: ")
        isbn = input("Ingrese el ISBN del libro a devolver: ")
        
        if id_usuario not in self.usuarios:
            print(f"No se encontró un usuario con ID {id_usuario}.")
            return
        
        usuario = self.usuarios[id_usuario]
        libro_a_devolver = None
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                libro_a_devolver = libro
                break
        
        if libro_a_devolver:
            usuario.libros_prestados.remove(libro_a_devolver)
            self.libros_disponibles[isbn] = libro_a_devolver
            print(f"Libro '{libro_a_devolver.detalle[0]}' devuelto por '{usuario.nombre}'.")
        else:
            print(f"El usuario no tiene prestado un libro con ISBN {isbn}.")
    
    def buscar_libro(self):
        criterio = input("Buscar por (titulo, autor, categoria): ").lower()
        valor = input(f"Ingrese el valor para buscar por {criterio}: ").lower()
        encontrados = []
        
        for libro in self.libros_disponibles.values():
            if criterio == "titulo" and valor in libro.detalle[0].lower():
                encontrados.append(libro)
            elif criterio == "autor" and valor in libro.detalle[1].lower():
                encontrados.append(libro)
            elif criterio == "categoria" and valor in libro.categoria.lower():
                encontrados.append(libro)
        
        if encontrados:
            print("Libros encontrados:")
            for libro in encontrados:
                print(f"Titulo: {libro.detalle[0]}, Autor: {libro.detalle[1]}, Categoría: {libro.categoria}, ISBN: {libro.isbn}")
        else:
            print(f"No se encontraron libros bajo el criterio '{criterio}' con valor '{valor}'.")
    
    def listar_libros_prestados(self):
        id_usuario = input("Ingrese el ID del usuario: ")
        
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            if usuario.libros_prestados:
                print(f"Libros prestados a '{usuario.nombre}':")
                for libro in usuario.libros_prestados:
                    print(f"Titulo: {libro.detalle[0]}, Autor: {libro.detalle[1]}, ISBN: {libro.isbn}")
            else:
                print(f"'{usuario.nombre}' no tiene libros prestados.")
        else:
            print(f"No se encontró un usuario con ID {id_usuario}.")

# Función para limpiar la pantalla
def limpiar_pantalla():
    print("\n" * 100)

# Crear una instancia de la biblioteca y probar las funcionalidades
def menu():
    while True:
        limpiar_pantalla()
        print("\n*****************************************UEA*****************************************")
        print("\n***********************Facultad de  ciencias de la computacion****************")
        print("\n**********************INGENIERIA EN SISTEMAS DE LA INFORMACION****************")
        print("\n******************************************************************************")
        print("\n******************************Sistema de Biblioteca***************************")
        print("\n******************************Menú de Biblioteca******************************")
        print("********************************1. Agregar Libro********************************")
        print("********************************2. Quitar Libro*********************************")
        print("********************************3. Registrar Usuario****************************")
        print("********************************4. Dar de Baja Usuario**************************")
        print("********************************5. Prestar Libro********************************")
        print("********************************6. Devolver Libro*******************************")
        print("********************************7. Buscar Libro*********************************")
        print("********************************8. Listar Libros Prestados**********************")
        print("********************************9. Salir****************************************")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            biblioteca.agregar_libro()
        elif opcion == "2":
            biblioteca.quitar_libro()
        elif opcion == "3":
            biblioteca.registrar_usuario()
        elif opcion == "4":
            biblioteca.dar_de_baja_usuario()
        elif opcion == "5":
            biblioteca.prestar_libro()
        elif opcion == "6":
            biblioteca.devolver_libro()
        elif opcion == "7":
            biblioteca.buscar_libro()
        elif opcion == "8":
            biblioteca.listar_libros_prestados()
        elif opcion == "9":
            break
        else:
            print("Opción no válida, intente de nuevo.")

biblioteca = Biblioteca()
menu()

