import flet as ft
import Shuffle

def PedirCarta(row_cartas, mostrar, CartasPlayer):
    cartaTupla = Shuffle.CartaAleatoria()  # Obtener una carta aleatoria
    if mostrar:
        nueva_carta = ft.Image(src=cartaTupla[0], width=100, height=100, fit=ft.ImageFit.CONTAIN)
    else:
        nueva_carta = ft.Image(src="assets/images/card_back0.png", width=100, height=100, fit=ft.ImageFit.CONTAIN)

    CartasPlayer.append(cartaTupla[1])  # Almacena el valor de la carta

    # Añadir la nueva carta al Row
    row_cartas.controls.append(nueva_carta)
    row_cartas.update()
    
    #return cartaTupla[0]


def MostrarCartasDeOtrosJugadores(ListaDeJugadores, ip_actual, row_jugadores):
    
    # Recorremos cada jugador en la lista
    for jugador in ListaDeJugadores:
        ip_jugador = jugador[1]
        
        # Si no es el jugador actual
        if ip_jugador != ip_actual:
            row_cartas_Player = row_jugadores.controls[ListaDeJugadores.index(jugador)].controls[0]  # Obtenemos el Row de sus cartas
            
            # Recorremos sus cartas
            for carta in jugador[2]:
                if not carta['mostrando_anverso']:  # Si la carta está boca abajo
                    carta['mostrando_anverso'] = True  # Cambiamos el estado
                    row_cartas_Player.controls.clear()  # Limpiamos para actualizar visualmente
                    nueva_carta = ft.Image(src=carta['anverso_src'], width=100, height=100, fit=ft.ImageFit.CONTAIN)
                    row_cartas_Player.controls.append(nueva_carta)  # Agregamos la carta visible
                    row_cartas_Player.update()  # Actualizamos la interfaz
