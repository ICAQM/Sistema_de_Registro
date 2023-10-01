import json

def cargar_tareas():
    try:
        with open('tareas.json', 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def guardar_tareas(tareas):
    with open('tareas.json', 'w') as archivo:
        json.dump(tareas, archivo)

def agregar_tarea(titulo, descripcion, tareas):
    nueva_tarea = {"titulo": titulo, "descripcion": descripcion, "completada": False}
    tareas.append(nueva_tarea)
    guardar_tareas(tareas)
    print("Tarea agregada correctamente.")

def listar_tareas(tareas):
    for i, tarea in enumerate(tareas):
        print(f"{i+1}. Título: {tarea['titulo']}, Descripción: {tarea['descripcion']}, Completada: {tarea['completada']}")

def completar_tarea(indice, tareas):
    if 0 <= indice < len(tareas):
        tareas[indice]["completada"] = True
        guardar_tareas(tareas)
        print("Tarea marcada como completada.")
    else:
        print("Índice inválido.")

def menu():
    tareas = cargar_tareas()

    while True:
        print("\n----- Menú -----")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Marcar tarea como completada")
        print("4. Salir")

        opcion = input("Ingrese el número de la opción que desea realizar: ")

        if opcion == '1':
            titulo = input("Ingrese el título de la tarea: ")
            descripcion = input("Ingrese la descripción de la tarea: ")
            agregar_tarea(titulo, descripcion, tareas)
        elif opcion == '2':
            listar_tareas(tareas)
        elif opcion == '3':
            indice = int(input("Ingrese el número de la tarea que desea marcar como completada: ")) - 1
            completar_tarea(indice, tareas)
        elif opcion == '4':
            break
        else:
            print("Opción inválida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    menu()
