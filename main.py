from users import UserCRUD

# Example Usage
if __name__ == "__main__":
    user_crud = UserCRUD()
    
    print("1 = Crear usuario")
    print("2 = Consultar usuario")
    print("3 = Actualizar usuario")
    print("4 = Eliminar usuario")
    option = int(input('Ingrese la seleccion deseada:\n'))
    
    # Create a new user
    if option == 1:
        id_document = int(input("Ingrese el numero de identificacion:\n"))
        name = input("Ingrese su nombre o el nombre de la empresa:\n")
        mail = input("Ingrese su correo electronico:\n")
        password = input("Ingrese su contrasena:\n")
        response = user_crud.create_user(id_document, name, mail, password)
        print(response)
    
    # Get user details
    elif option == 2:
        id_document = int(input("Ingrese el numero de identificacion a consultar:\n"))
        user_details = user_crud.get_user(id_document)
        print(user_details)
    
    # Update user information
    elif option == 3:
        update_response = user_crud.update_user(1234567890, nombre="Updated User", email="updateduser@example.com")
        print(update_response)
    
    # Delete user
    elif option == 4:
        id_document = int(input("Ingrese el numero de identificacion del usuario a eliminar:\n"))
        delete_response = user_crud.delete_user(id_document)
        print(delete_response)
