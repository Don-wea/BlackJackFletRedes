import flet as ft
import Shuffle

CartasCasino = []
sourceCartaAbajo = ""  # Guardamos el source de la carta boca abajo
valorCartaAbajo = 0    # Guardamos el valor de la carta boca abajo
carta_abajo_imagen = None  # Referencia a la imagen de la carta boca abajo


def CasinoInicia(row_cartas):
    # Pedir dos cartas al inicio, una de ellas boca abajo
    PedirCarta(row_cartas, True)
    PedirCarta(row_cartas, False)  # Esta es la carta que estará boca abajo
    return CartasCasino


def PedirCarta(row_cartas, mostrar):
    global sourceCartaAbajo, valorCartaAbajo, carta_abajo_imagen
    
    cartaTupla = Shuffle.CartaAleatoria()  # Obtener una carta aleatoria
    
    
    if mostrar:
        nueva_carta = ft.Image(src=cartaTupla[0], width=100, height=100, fit=ft.ImageFit.CONTAIN)
        CartasCasino.append(cartaTupla[1])     # Almacena el valor de la carta
    else:
        # Guardamos los detalles de la carta boca abajo
        sourceCartaAbajo = cartaTupla[0]
        valorCartaAbajo = cartaTupla[1]
        
        CartasCasino.append(0)     # Almacena el valor de la carta
        
        # La carta boca abajo será la carta reverso
        carta_abajo_imagen = ft.Image(src="assets/images/card_back0.png", width=100, height=100, fit=ft.ImageFit.CONTAIN)
        nueva_carta = carta_abajo_imagen
    
    # Añadir la nueva carta al Row
    row_cartas.controls.append(nueva_carta)
    
    # Actualizar la página para reflejar los cambios
    row_cartas.update()
    
    puntaje = Shuffle.CalcularPuntaje(CartasCasino)
    return puntaje


def CierreApuestas():
    global carta_abajo_imagen, sourceCartaAbajo, valorCartaAbajo
    
    # Voltear la carta boca abajo
    if carta_abajo_imagen:
        carta_abajo_imagen.src = sourceCartaAbajo
        carta_abajo_imagen.update()
    
        CartasCasino[1] = valorCartaAbajo
        return CartasCasino
        # Recalcular el puntaje
    #    nuevo_puntaje = Shuffle.CalcularPuntaje(CartasCasino)

        
        # Actualizar el texto del puntaje
        # TextoPuntaje.value = f"Puntaje {nuevo_puntaje}"
        # TextoPuntaje.update()
        
    #if len(CartasCasino) == 2 and nuevo_puntaje == 21:
    #    print("BLACKJACK!")




