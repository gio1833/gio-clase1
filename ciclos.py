# # primer ejercicio

# ace= 0
# dec= 11

# while ace < 10:
#     ace +=1
#     dec -=1
#     print(ace, '/', dec)


#ejercicio 2


import random       

aleatoreo = random.randint(1,100)

adivina = 0

while adivina != aleatoreo:
   
    if adivina == 0:
        print('inicia el juego')
    elif adivina < aleatoreo:
        print('demasiado bajo')
    else:
        print('demasiado alto')

    adivina = int(input('ingrese el numero'))  
   
print('haz ganado')