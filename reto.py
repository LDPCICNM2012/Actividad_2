operacion = input("introduce la operacion que quieres realizar (+/-): ")
Numeros = int(input("introduce el número de números que quieres operar: "))

lista = []
for i in range(Numeros):
    lista.append(int(input("introduce un numero: ")))

resta = 0
suma = 0
if operacion == "+":
    for num in lista:
        suma = suma + num
    print(suma)
    
    

elif operacion == "-":
    for num in lista:
        resta = resta - num
    print(resta)






