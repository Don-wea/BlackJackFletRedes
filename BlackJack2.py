import flet as ft
import Shuffle
import Casino
import Player

class BlackjackApp:
    def __init__(self):
        self.page = None

    def iniciar_ventana(self, page: ft.Page):
        self.page = page
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        
        # Calcula el puntaje de las cartas y las retorna
    def calcular_puntaje(self, cartas):
        return Shuffle.CalcularPuntaje(cartas)
    
        # Agrega texto a la ventana y devuelve la instancia
    def agregar_texto(self, texto):
        mensaje_texto = ft.Text(value=texto, size=20)
        self.page.add(mensaje_texto)
        return mensaje_texto
    
        # Recibe un modulo de texto y actualiza su contenido
    def actualizar_texto(self, modulo_texto, nuevo_texto):
        modulo_texto.value = nuevo_texto
        modulo_texto.update()
        
        # Devuelve el puntaje de las cartas iniciales Y las cartas fisicas
    def casino_inicia(self):
        row_cartas_casino = ft.Row(alignment=ft.MainAxisAlignment.CENTER)
        self.page.add(row_cartas_casino)

        # Agregar cartas del casino
        cartas_casino = Casino.CasinoInicia(row_cartas_casino)
        return [cartas_casino, row_cartas_casino]
    
        # Se le puede pasar el Modulo de un texto mas su nuevo contenido para linkear la accion con la visualizacion del puntaje
    def casino_pide_carta(row_cartas_Casino, ModuloTexto = None, NuevoTexto = None):
        puntaje = Casino.PedirCarta(row_cartas_Casino, True)
        if ModuloTexto != None and NuevoTexto != None:
            NuevoTexto = NuevoTexto + f" {puntaje}"
            ModuloTexto.value = NuevoTexto
            ModuloTexto.update()
            
        # Da vuelta la carta del casino
    def casino_muestra_carta():
        Casino.CierreApuestas()
        
        # Agrega un boton a la ventana que pide cartas a la mano del Casino
        # Si se le pasa un Modulo de texto y su nuevo contenido, actualizara ese texto y le agregara el nuevo puntaje
    def agregar_boton_casino_pide_carta(self, texto, row_cartas_Casino, ModuloTexto = None, NuevoTexto = None):
        if ModuloTexto != None and NuevoTexto != None:
            nuevoBoton = ft.ElevatedButton(text=texto, on_click=lambda _:self.CasinoPideCarta(row_cartas_Casino, ModuloTexto, NuevoTexto))
            self.page.add(nuevoBoton)
        else:
            nuevoBoton = ft.ElevatedButton(text=texto, on_click=lambda _:self.CasinoPideCarta(row_cartas_Casino))
            self.page.add(nuevoBoton)
            
            # Agrega un boton en la ventana que da vuelta la carta inicial del Casino        
    def AgregarBotonCasinoMuestraCarta(self, texto):
        nuevoBoton = ft.ElevatedButton(text=texto, on_click=lambda _: self.CasinoMuestraCarta())
        self.page.add(nuevoBoton)
        
        # Crea la fila en la que iran los jugadores, se devuelve la fila para poder hacer cambios en los jugadores
    def CrearInstanciaDeJugadores(self):
        row_jugadores = ft.Row(alignment=ft.MainAxisAlignment.CENTER, spacing=30)
        self.page.add(row_jugadores)
        return row_jugadores
    
        # Agrega un nuevo jugador a la lista de jugadores
    def AgregarJugador(self, nombre, ip, jugadores):
        nuevoJugador = [nombre, ip]
        jugadores.append(nuevoJugador)
        
        # Inicializa el jugador, dandole atributos y cartas. Recibe la Ip del jugador que juega la partida, no la del jugador   
    def JugadorInicia(Jugador, row_jugadores, ip_actual):
        row_cartas_Player = ft.Row(alignment=ft.MainAxisAlignment.CENTER)

        columna_jugador = ft.Column(
            controls=[
                row_cartas_Player,
                ft.Text(value=f"Player {Jugador[0]}", size=20),  # Nombre del jugador
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )

        row_jugadores.controls.append(columna_jugador)
        row_jugadores.update()

        # Si el jugador es el mismo que la ip entonces retorna True
        mostrar_cartas = Jugador[1] == ip_actual

        CartasJugador = []
        Player.PedirCarta(row_cartas_Player, mostrar_cartas, CartasJugador)
        Player.PedirCarta(row_cartas_Player, mostrar_cartas, CartasJugador)
        Jugador.append(CartasJugador)
        Jugador.append(mostrar_cartas)
        print(f"Cartas actuales del jugador: {Jugador}")
        
    