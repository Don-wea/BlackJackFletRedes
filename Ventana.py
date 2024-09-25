import flet as ft
import Casino
import Player

def main(page: ft.Page):
    
    # Definimos los jugadores con sus nombres y IDs
    Players = [["ASD", 192], ["JUAN", 200], ["CARL", 300]]
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Inicializamos el Row que contendrá las cartas del Casino
    row_cartas_Casino = ft.Row(alignment=ft.MainAxisAlignment.CENTER)
    page.add(row_cartas_Casino)

    # Agregar cartas del inicio del Casino
    CartasCasino = Casino.CasinoInicia(row_cartas_Casino)
    page.add(ft.Text(value="Casino", size=20))

    # Mostrar el puntaje inicial del casino
    puntaje = Casino.Shuffle.CalcularPuntaje(CartasCasino)
    TextoPuntaje = ft.Text(value=f"Puntaje {puntaje}", size=20)
    page.add(TextoPuntaje)

    # Función para agregar una carta al Casino
    def agregar_carta(_):
        Casino.PedirCarta(row_cartas_Casino, True)
        nuevo_puntaje = Casino.Shuffle.CalcularPuntaje(CartasCasino)
        TextoPuntaje.value = f"Puntaje {nuevo_puntaje}"
        TextoPuntaje.update()

    def cerrar_apuestas():
        Casino.CierreApuestas()
        nuevo_puntaje = Casino.Shuffle.CalcularPuntaje(CartasCasino)
        TextoPuntaje.value = f"Puntaje {nuevo_puntaje}"
        TextoPuntaje.update()

    # Botones para agregar carta y cerrar apuestas
    boton_agregar = ft.ElevatedButton(text="Agregar carta", on_click=agregar_carta)
    boton_mostrar = ft.ElevatedButton(text="Cerrar Apuestas", on_click=lambda _: cerrar_apuestas())

    page.add(boton_agregar)
    page.add(boton_mostrar)

    row_jugadores = ft.Row(alignment=ft.MainAxisAlignment.CENTER, spacing=30)
    page.add(row_jugadores)

    # Para cada jugador, crear su propia lista de cartas y mostrar sus cartas y puntaje
    for jugador in Players:
        row_cartas_Player = ft.Row(alignment=ft.MainAxisAlignment.CENTER)

        columna_jugador = ft.Column(
            controls=[
                row_cartas_Player,
                ft.Text(value=f"Player {jugador[0]}", size=20),  # Nombre del jugador
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )

        row_jugadores.controls.append(columna_jugador)
        row_jugadores.update()

        # Inicializar una lista vacía de cartas para cada jugador
        CartasPlayer = []

        # Asignar dos cartas iniciales a cada jugador (una a una para asegurarnos de que se mantengan en su lista)
        Player.PedirCarta(row_cartas_Player, True, CartasPlayer)
        Player.PedirCarta(row_cartas_Player, True, CartasPlayer)
        print(f"Cartas actuales del jugador: {CartasPlayer}")  # Verificar que solo este jugador acumula cartas

        #CartasPlayer.append(primera_carta)
        #CartasPlayer.append(segunda_carta)

        # Añadir las cartas del jugador a su entrada en la lista 'Players'
        jugador.append(CartasPlayer)  # Esto asegura que cada jugador tenga su propio array
        

        # Calcular el puntaje y mostrarlo debajo del nombre del jugador
        puntaje_jugador = Player.Shuffle.CalcularPuntaje(CartasPlayer)
        print(f"puntaje es :{puntaje_jugador}")
        columna_jugador.controls.append(ft.Text(value=f"Puntaje: {puntaje_jugador}", size=20))

    page.update()

ft.app(main)



