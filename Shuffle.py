import flet as ft
import random


numeros = ['A','2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
pinta = ["clubs","diamonds","hearts","spades"]

def Valor(numero):
    if numero == "A":
        valor = 11  # El valor del As inicialmente es 11
    elif numero in ["J", "Q", "K"]:
        valor = 10
    else:
        valor = int(numero)
    return valor


def CartaAleatoria():
    source = "assets/images/"
    numero = random.choice(numeros)
    source = source + numero +"_"
    source = source + random.choice(pinta)+".svg"
    valor = Valor(numero)
    carta = [source, valor]
    return carta

def CalcularPuntaje(cartas):
    ases = 0  # Contador de ases
    puntaje = 0
    perder = False
    
    for carta in cartas:
        puntaje += carta
        if carta == 11:  # Verificamos si es un As
            ases += 1
    
    # Ajustar el puntaje si supera 21 y tenemos ases
    while puntaje > 21 and ases > 0:
        puntaje -= 10  # Cambiar el As de 11 a 1
        ases -= 1
    
    if puntaje > 21:
        perder = True
    
    if perder:
        print("PERDISTE")
    
    return puntaje
