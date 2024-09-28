from BlackJack2 import BlackjackApp as BJ
import flet as ft

def main(page: ft.Page):
    app = BJ()
    Basura = []
    
    app.iniciar_ventana(page)
    app.agregar_texto("Casino\n")
    
    casino = []
    casino = app.casino_inicia()
    puntaje_casino = app.agregar_texto(f"Puntaje: {app.calcular_puntaje(casino[0])}")
    app.agregar_boton_casino_muestra_carta("BOTON MOSTRAR", puntaje_casino, "Puntaje: ")
    app.agregar_boton_casino_pide_carta("asd", casino[1], puntaje_casino, "Puntaje: ")
    app.agregar_texto("\nJugadores")
    
    lista_jugadores = []
    row_jugadores = []
    
    row_jugadores = app.crear_instancia_de_jugadores()
    
    app.agregar_jugador("Juan","192.168.1.50", lista_jugadores)
    app.agregar_jugador("Juan2","192.168.1.500", lista_jugadores)
    app.agregar_jugador("Juan3","192.168.12.500", lista_jugadores)
    print(f"LISTA {lista_jugadores}\n")
    
    for i in range(len(lista_jugadores)):
        x = app.jugador_inicia(lista_jugadores[i], row_jugadores)
        player = x[0]
        row_cartas = x[1]
        texto_puntaje = f"Puntaje: {app.calcular_puntaje(lista_jugadores[i][2])}"
        modulo_puntaje = app.crear_texto(texto_puntaje)
        
        app.modificar_saldo_jugador(lista_jugadores[i], 500)
        texto_saldo = app.crear_texto(f"Saldo: {app.obtener_saldo_jugador(lista_jugadores[i])}")
        app.agregar_elemento_visual_jugador(player, texto_saldo)
        
        app.agregar_elemento_visual_jugador(player, modulo_puntaje)
        lista_jugadores[i].append(row_cartas)
        lista_jugadores[i].append(modulo_puntaje)
        lista_jugadores[i].append(texto_saldo)
        
        print(lista_jugadores[0])
    
    
    
ft.app(target=main)