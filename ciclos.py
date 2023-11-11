# numero = int (input('ingrese un numero entero'))

# if (numero % 2) == 0:
#     print ('Es par')
# else:
#     print('Es impar')

# edad= int(input('ingrese la edad' ))

# if edad < 18:
#     print ('Eres menor de edad')    
# elif edad >= 18 and edad <=65:
#     print ('Eres un adulto')
# else: 
#     print('Eres un adulto mayor')


# #ejercicio 3

# precio= int (input('ingrese  el precio del producto'))
# edad= int (input('ingrese la edad'))   

# if edad < 18:
#     descuentoMe= (precio *10)/100    
#     total= print ('el descuento es del 10% y el precio total a pagar es:', precio descuentoMe)    
# elif edad= >= 65:
#     descuentoMa= (precio *15)/100
#     total= print (' el descuento es del 15% ty el precio total a pagar es:', precio descuentoMa)
# elif edad >18 and edad < 65:
#     total= 'no tiene descuento'
#     print(total)    

# #ejercicio 4

# Puntuacion = (input('ingrese una puntacion'))

# if Puntuacion >= 90 and Puntuacion <= 100:
#      print ("A"('sobresaliente'))
# elif Puntuacion >= 80 and Puntuacion <= 89:
#     print("B"('bueno')) 
# elif Puntuacion >= 70 and Puntuacion <= 79:
#     print("C"('satisfactorio'))
# elif Puntuacion >= 60 and Puntuacion <= 69:
#     print("D"('necesita mejorar'))
# elif Puntuacion < 60:
#     print ("F"('reprobado'))             


# #ejercio 5

# salario = int(input('ingrese su salario anual'))

# if salario <= 10000:
#     paga= print('no se aplica impuesto')
    
# elif salario > 10000 and salario <= 50000:
#     impuesto = (salario*10)/100
#     paga = print('si su impuesto es el 10% de su salario, debe págar', impuesto)

# elif salario > 50000 and salario <= 100000:
#     impuesto = (salario *20)/100
#     paga= print(' si su impuesto es el 20% de su salario, debe pagar ', impuesto)       

# elif salario > 100000:
#     impuesto = (salario *30)/100
#     paga= print('si su impuesto es el 30% debe pagar', impuesto)


# 1 ejercicio 

# asc = 0
# desc = 10

# while asc < 10:
#     asc += 1
#     desc -=10
#     print(asc, '/', desc)

# # 2ejercicio

# import random

# aleatoreo = random.randint(1,100)

# adivina = 0 

# while adivina != aleatoreo:

#     if adivina ==0:
#         print('inicia el juego')        
#     elif adivina < aleatoreo:
#         print('demasiado bajo')
#     else:
#         print('demasiado alto')

#     adivina = int(input('ingrese el numero'))

# print('haz ganado')

# 3 ejercio tabla de multiplicar

# numero = int(input('ingresar un numero'))

# for i in range (1, 11):
#     resultado = i * numero
#     print(numero, "X", i, "=", resultado)

# 4 ejercicio suma de numero pares

# num = int (input("escriba un numero"))

# if num % 2 == 0:
#     print('es par')
# else:
#     print('es impar')


# 4 ejercicio patron de astterisco

# n= int(input('escriba el numero de patrones de asteriscos'))
# for num in range(5):
#     print("*" * num)

# sexto ejercicio suna de numero pares con "for"" y "if"

# suma = 0
# a = int(input('Num inicial:'))
# b = int(input('Nun final:'))
 
# for i in range(b, a + 1):
#     if i % 2 == 0:
#         suma += i
#     print('\a La suma es ',suma)

# septimo ejercicio contador de vocales 
# i = 0
# contador = 0
# while i < len('palabra'):
#     if ('palabra[i] == vocales'):
#         Contador = Contador + 1
#     i = i + 1

# octavo ejercicio numeros primos
 
# numero = int(input("Ingrese un numero"))

# es_primo = True

# if numero > 1:
#     for i in range(2, int(numero**0.5) + 1):
#         if numero % i == 0:
#             es_primo = False
#             break

# if es_primo and numero > 1:
#     print(f"{numero} es un numero primo,")  
# else:
#     print(f"{numero} no es un numero primo,") 

# noveno ejercicio adivine el numero secreto

# import random
# numero_secreto = random.randint(1,100)

# print("¡¡¡Bienvenido al juego!!!")
# intentos = 0

# while True:
#     intentos =int(input('ingrese el numero: '))
#     intentos += 1 

#     if intentos == numero_secreto:
#       print('El número es mas pequeño')
#     elif intentos < numero_secreto:
#         print('El número es mas grande')

# print('Felicidades has adivinado que el número secreto es:',numero_secreto)

# Decimo Ejercicio generador de patrones

# numero = int(input("Ingrse un numero"))     

# if numero % 2 == 0:
#     print("*" * numero)
# else:
#     for i in range(numero):
#         print("*" *(i + 1))      










