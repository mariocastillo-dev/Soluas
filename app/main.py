from app.crud.user_crud import UserCRUD
from app.core.database import SessionLocal

# Example Usage
if __name__ == "__main__":
    # Crear una sesión de la base de datos
    db = SessionLocal()
    user_crud = UserCRUD(db)
    
    try:
        print("1 = Crear usuario")
        print("2 = Listar todos los usuarios")
        print("3 = Actualizar usuario")
        print("4 = Eliminar usuario")
        option = int(input('Ingrese la seleccion deseada:\n'))

        # Crear un nuevo usuario
        if option == 1:
            id_document = int(input("Ingrese el numero de identificacion:\n"))
            name = input("Ingrese su nombre o el nombre de la empresa:\n")
            mail = input("Ingrese su correo electronico:\n")
            password = input("Ingrese su contrasena:\n")
            role_name = input("Ingrese el rol del usuario (Admin, User, Customer):\n")
            response = user_crud.create_user(id_document, name, mail, password, role_name)
            print(response)

        # Listar todos los usuarios
        elif option == 2:
            users = user_crud.get_all_users()
            if isinstance(users, str):
                print(users)  # Para mostrar errores si ocurren
            else:
                for user in users:
                    print(f"ID: {user.ID_documento}, Nombre: {user.nombre}, Email: {user.email}, Rol ID: {user.role_id}")

        # Actualizar información de un usuario
        elif option == 3:
            id_document = int(input("Ingrese el numero de identificacion del usuario a actualizar:\n"))
            nombre = input("Ingrese el nuevo nombre del usuario:\n")
            email = input("Ingrese el nuevo correo electrónico del usuario:\n")
            update_response = user_crud.update_user(id_document, nombre=nombre, email=email)
            print(update_response)

        # Eliminar usuario
        elif option == 4:
            id_document = int(input("Ingrese el numero de identificacion del usuario a eliminar:\n"))
            delete_response = user_crud.delete_user(id_document)
            print(delete_response)

    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")
    finally:
        # Cerrar la sesión de la base de datos
        db.close()
