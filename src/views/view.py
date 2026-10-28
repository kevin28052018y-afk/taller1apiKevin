import os
import httpx
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener y proteger la URL base de la API desde las variables de entorno
BASE_URL = os.getenv("BASE_URL")

if not BASE_URL:
    raise RuntimeError("La variable BASE_URL no está definida. Revisa tu archivo .env")

# Asegurar que no termine con barra diagonal para evitar doble slash en las rutas
BASE_URL = BASE_URL.rstrip("/")


def listar_aprendices():
    try:
        response = httpx.get(f"{BASE_URL}/trainees")
        if response.status_code == 200:
            aprendices = response.json()
            if not aprendices:
                print("No hay aprendices registrados.")
                return

            print("\n--- Lista de Aprendices ---")
            for a in aprendices:
                print(
                    f"ID: {a['id']} | Documento: {a['document']} | "
                    f"Nombre: {a['firstname']} {a['lastname']} | "
                    f"Correo: {a['email']} | Edad: {a['age']} | "
                    f"Programa: {a['program']} | Ficha: {a['record_number']}"
                )
        else:
            print("Error al obtener aprendices:", response.text)
    except Exception as e:
        print(f"Error de conexión: {e}")


def buscar_aprendiz():
    trainee_id = input("Ingresa el ID del aprendiz: ").strip()
    try:
        response = httpx.get(f"{BASE_URL}/trainees/{trainee_id}")
        if response.status_code == 200:
            a = response.json()
            print("\n--- Datos del Aprendiz ---")
            print(f"ID: {a['id']}")
            print(f"Documento: {a['document']}")
            print(f"Nombre: {a['firstname']} {a['lastname']}")
            print(f"Correo: {a['email']}")
            print(f"Edad: {a['age']}")
            print(f"Programa: {a['program']}")
            print(f"Ficha: {a['record_number']}")
        else:
            print("Error:", response.json().get("detail", "Aprendiz no encontrado"))
    except Exception as e:
        print(f"Error de conexión: {e}")


def crear_aprendiz():
    print("\n--- Registrar Aprendiz ---")
    try:
        document = input("Documento: ").strip()
        firstname = input("Nombre: ").strip()
        lastname = input("Apellido: ").strip()
        email = input("Correo: ").strip()
        age = int(input("Edad: ").strip())
        program = input("Programa: ").strip()
        record_number = int(input("Ficha: ").strip())

        data = {
            "document": document,
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "age": age,
            "program": program,
            "record_number": record_number,
        }

        response = httpx.post(f"{BASE_URL}/trainees", json=data)
        if response.status_code == 201:
            print("Aprendiz registrado con éxito.")
        else:
            print("Error al registrar:", response.text)
    except ValueError:
        print("Error: Edad y Ficha deben ser números enteros.")
    except Exception as e:
        print(f"Error de conexión: {e}")


def actualizar_aprendiz():
    print("\n--- Actualizar Aprendiz ---")
    trainee_id = input("Ingresa el ID del aprendiz a actualizar: ").strip()

    print("Deja el campo vacío si no deseas modificarlo:")
    firstname = input("Nuevo nombre: ").strip()
    lastname = input("Nuevo apellido: ").strip()
    email = input("Nuevo correo: ").strip()
    age_input = input("Nueva edad: ").strip()
    program = input("Nuevo programa: ").strip()
    record_number_input = input("Nueva ficha: ").strip()

    data = {}
    if firstname:
        data["firstname"] = firstname
    if lastname:
        data["lastname"] = lastname
    if email:
        data["email"] = email
    if age_input:
        try:
            data["age"] = int(age_input)
        except ValueError:
            print("Error: La edad debe ser un número entero.")
            return
    if program:
        data["program"] = program
    if record_number_input:
        try:
            data["record_number"] = int(record_number_input)
        except ValueError:
            print("Error: La ficha debe ser un número entero.")
            return

    if not data:
        print("No se ingresaron datos para actualizar.")
        return

    try:
        response = httpx.put(f"{BASE_URL}/trainees/{trainee_id}", json=data)
        if response.status_code == 200:
            print("Aprendiz actualizado con éxito.")
        else:
            print("Error al actualizar:", response.text)
    except Exception as e:
        print(f"Error de conexión: {e}")


def eliminar_aprendiz():
    print("\n--- Eliminar Aprendiz ---")
    trainee_id = input("Ingresa el ID del aprendiz a eliminar: ").strip()
    try:
        response = httpx.delete(f"{BASE_URL}/trainees/{trainee_id}")
        if response.status_code == 200:
            print("Aprendiz eliminado con éxito.")
        else:
            print("Error:", response.json().get("detail", "No se pudo eliminar"))
    except Exception as e:
        print(f"Error de conexión: {e}")


def menu():
    while True:
        print("\n=== MENÚ APRENDICES ===")
        print("1. Listar aprendices")
        print("2. Buscar aprendiz por ID")
        print("3. Crear aprendiz")
        print("4. Actualizar aprendiz")
        print("5. Eliminar aprendiz")
        print("6. Salir")

        opcion = input("Selecciona una opción (1-6): ").strip()

        if opcion == "1":
            listar_aprendices()
        elif opcion == "2":
            buscar_aprendiz()
        elif opcion == "3":
            crear_aprendiz()
        elif opcion == "4":
            actualizar_aprendiz()
        elif opcion == "5":
            eliminar_aprendiz()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta nuevamente.")


if __name__ == "__main__":
    menu()
