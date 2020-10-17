def clave(cadena):
        requisitos = True
        esp = False
        mayus = False
        minus = False
        num = False
        if len(cadena) < 8:
                print("La contraseña debe contener un mínimo de 8 caracteres")
                requisitos = False
        if cadena.isalnum()== True:
                print("La contraseña debe contener 1 carácter no alfanumérico")
                requisitos = False                    
        for carac in cadena:                
                if carac.isspace()==True:
                        esp = True
                if carac.isupper()== True:
                        mayus = True
                if carac.islower()== True:
                        minus = True
                if carac.isdigit()== True:
                        num = True
        if esp == True:
                print("La contraseña no puede contener espacios en blanco")
                requisitos = False
        if mayus == False:
                print("La contraseña debe contener letras mayúsculas")
                requisitos = False
        if minus == False:
                print("La contraseña debe contener letras minúsculas")
                requisitos = False
        if num == False:
                print("La contraseña debe contener números")
                requisitos = False
        if requisitos == False:
           print("La contraseña elegida no es segura")
        return requisitos
