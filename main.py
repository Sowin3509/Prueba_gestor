from services.gestor_usuarios import GestorUsuarios
from services.gestor_tareas import GestorTareas

gestor_usuarios = GestorUsuarios()
gestor_tareas = GestorTareas()


def main():
    print("Bienvenido al Gestor de Tareas")

    while True:
        print("\n1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            username = input("Ingrese un nombre de usuario: ")
            password = input("Ingrese una contraseña: ")
            if gestor_usuarios.registrar_usuario(username, password):
                print("Usuario registrado exitosamente.")
            else:
                print("Error: El usuario ya existe.")

        elif opcion == "2":
            username = input("Ingrese su usuario: ")
            password = input("Ingrese su contraseña: ")
            usuario_id = gestor_usuarios.autenticar_usuario(username, password)

            if usuario_id:
                print(f"Bienvenido, {username}!")
                while True:
                    print("\n1. Agregar tarea")
                    print("2. Ver tareas")
                    print("3. Actualizar tarea")
                    print("4. Eliminar tarea")
                    print("5. Cerrar sesión")
                    opcion_tareas = input("Seleccione una opción: ")

                    if opcion_tareas == "1":
                        descripcion = input("Descripción de la tarea: ")
                        categoria = input("Categoría: ")
                        gestor_tareas.agregar_tarea(usuario_id, descripcion, categoria)
                        print("Tarea agregada.")

                    elif opcion_tareas == "2":
                        tareas = gestor_tareas.obtener_tareas(usuario_id)
                        for tarea in tareas:
                            print(f"[{tarea[0]}] {tarea[2]} - {tarea[3]} - {tarea[4]}")

                    elif opcion_tareas == "3":
                        tarea_id = int(input("ID de la tarea a actualizar: "))
                        nuevo_estado = input("Nuevo estado (Pendiente, Completada, En progreso): ")
                        gestor_tareas.actualizar_tarea(tarea_id, nuevo_estado)
                        print("Tarea actualizada.")

                    elif opcion_tareas == "4":
                        tarea_id = int(input("ID de la tarea a eliminar: "))
                        gestor_tareas.eliminar_tarea(tarea_id)
                        print("Tarea eliminada.")

                    elif opcion_tareas == "5":
                        print("Cerrando sesión...")
                        break

            else:
                print("Usuario o contraseña incorrectos.")

        elif opcion == "3":
            print("Saliendo...")
            break


if __name__ == "__main__":
    main()
