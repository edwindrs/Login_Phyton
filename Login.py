import ValidaUsuario
import ValidaPassword

correcto=False
while correcto==False:
    nombre=input("Ingrese su Usuario: ")
    if ValidaUsuario.usuario(nombre) == True:
        correcto=True
        
correcto=False  
while correcto==False:
    password=input("Ingrese su Contraseña: ")
    if ValidaPassword.clave(password) == True:
        correcto=True

print("Login Exitoso")
