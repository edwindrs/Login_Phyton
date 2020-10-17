def usuario(cadena):
        requisitos = True
        if cadena.isalnum()== False: 
                print("El nombre de usuario debe contener Solo letras y números")
                requisitos = False
            
        if len(cadena) < 6:
                print("El nombre de usuario debe contener al menos 6 caracteres")
                requisitos = False
            
        if len(cadena) > 12:
                print("El nombre de usuario no puede contener más de 12 caracteres")
                requisitos = False
        return requisitos
