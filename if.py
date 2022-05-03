# edad=int(input("Ingrese su edad"))

# if edad>= 18 :
#     print("es mayor de edad")
# elif edad <18 and edad>0 :
#     print("usted es menor de edad")
# else:
#     print("Vuelve a nacer peazo de logi")    


#actividad 2 con if ejercicio 01


user_1= "pedro"
pass_1="1234"
user_2="Angel"
pass_2="a4s1"

user_0=input("ingrese nombre usuario")
pass_0=input("ingrese clave usuario")

if user_1 == user_0 and pass_0 == pass_1 :
    print("Bienvenido Pedro")
    
elif user_2==user_0 and pass_0==pass_2 :
    print("Bienvenido Angel")
    
else:
    print("Credenciales Incorrectas")
    

