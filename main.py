from BlackJack2 import BlackjackApp as BJ
import flet as ft

def main(page: ft.Page):
    app = BJ()
    
    app.iniciar_ventana(page)
    app.agregar_texto("Casino\n")
    
    cartas_casino = []
    cartas_casino = app.casino_inicia()
    app.agregar_texto("\nJugadores")
    
    lista_jugadores = []
    app.AgregarJugador("Juan","192.168.1.50", lista_jugadores)
    print(lista_jugadores)
    app.JugadorInicia()
    
    
ft.app(target=main)