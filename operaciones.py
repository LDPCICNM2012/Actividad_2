print("Bienvenido a el programa de operaciones")
operacion = (int(input("Que operacion quieres hacer: 1. Suma  2. Resta  3. Multiplicar  4. Dividir")))
if operacion == 1:

    numeros_introducir = int(input("¿Cuantos numeros quieres introducir?: "))

    lista = []

    for i in range(numeros_introducir):
        numero = int(input("Introduce un numero: "))
        lista.append(numero)

    for x in lista:
        suma = suma + x




