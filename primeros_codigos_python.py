
def es_primo(numero):
    """ determina si un numero es primo

        numero int cualquier entero
        returns True o false
    """
    cantidad = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            cantidad = cantidad + 1

    if cantidad == 2:
        return True
    else:
        return False


def cantidad_primos(numero):
    """ muestra la cantidad de primos que hay hasta el numero dado

        numero int cualquier entero
        returns muestra dentro de la misma función
    """
    for i in range(1, numero + 1):
        cantidad = 0
        contador = 1
        while contador <= i:
            if i % contador == 0:
                cantidad = cantidad + 1

            contador += 1

        if cantidad == 2:
            print('Es primo = ' + str(i))


def es_par(numero):
    """ determina si un numero es par

        numero int cualquier entero
        returns True o False
    """ 
    if numero % 2==0:
        return True
    else:
        return False


def conversor(moneda, tasa):
    """ convierte un monto dado de una de las tres monedas a dolar 

        moneda string tres opciones 
        tasa float cualquier numero positivo
    """
    pesos = input("¿Cuantos "+ moneda + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos/tasa
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes USD" + dolares + " dolares")


def adivina_numero():
    """ Mini juego para adivinar un numero del 1 al 100, generado previamente de forma aleatoria
        
        no necesita param, ya que el unico numero (numero_elegido) se pide dentro de la funcion
    """        
    import random # para importar el modulo randon
    numero_aleatorio = random.randint(1, 100) #funcion randint (rand int) del modulo random
    numero_elegido = int(input('Elige un numero del 1 al 100: '))
    i=1
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            numero_elegido= int(input('Busca un numero mas grande: '))
        else:
            numero_elegido= int(input('Busca un numero mas pequeño: '))
        i+=1
    print('¡GANASTE!')
    print('En ' +str(i) +' intentos')


def main():
    """ funcion principal, menu de mini-proyectos
    """
    opcion = int(input('''     Que desea hacer?
        1. Adivina un numero
        2. Conversor de monedas
        3. Es par?
        4. Es primo?
        5. Generar una contraseña
        6. Comparar edad
        7. Enumeracion Exhaustiva
        8. Aproximacion
        9. Busqueda Binaria
        10. Factorial
        11.Fibonacci
     opcion: '''))

    if opcion == 1:
        print('******* Adivina un numero ******* ')
        adivina_numero()

    elif opcion == 2:
        opcion = 0
        while opcion < 1 or opcion > 3:
            print('******* Conversor de monedas ******* ')
            opcion = int(input('''Escoge la moneda que deseas convertir a dolares
                1. Bolivares
                2. Pesos Argentinos
                3. Pesos Chilenos )
                opcion: '''))
            if opcion == 1:
                conversor('Bolivares', 280000)
            elif opcion == 2:
                conversor('pesos Argentinos', 115)
            elif opcion == 3:
                conversor('pesos Chilenos', 730)
            else: 
                print('Elige una opcion valida')

    elif opcion == 3:
        print('******* Saber si un numero es par ******* ')
        numero=int(input("Introduzca un numero: "))
        if es_par(numero):
            print("Si es par")
        else:
            print("No es par")

    elif opcion == 4:
        opcion = 0
        while opcion < 1 or opcion > 2:
            print('******* Numeros primos ******* ')
            opcion = int(input('''             Que operacion desea hacer?
                1. Saber si un numero es primo
                2. Cantidad de primos hasta el numero dado
             opcion: '''))
            numero=int(input("Introduzaca un numero: "))
            if opcion == 1:
                if es_primo(numero):
                    print("Si es primo")
                else: 
                    print("No es primo")
            elif opcion == 2:
                cantidad_primos(numero)
            else: 
                print('Elige una opcion valida')



if __name__ == '__main__':
    main()