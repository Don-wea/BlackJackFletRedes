import flet as ft
import Shuffle
import Casino
import Player


    # Crea una ventana vacia y se inyecta el codigo del programador
def IniciarVentana(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    CodigoProgramador(page) ## <----- AQUI INICIA EL CODIGO QUE SE EJECUTA CUSTOM


    
    # Calcula el puntaje de las cartas y las retorna
def CalcularPuntaje(cartas):
    return Shuffle.CalcularPuntaje(cartas)


    # Agrega texto a la ventana y devuelve la instancia
def AgregarTexto(page ,texto):
    MensajeTexto = ft.Text(value=texto, size=20)
    page.add(MensajeTexto)
    return MensajeTexto

    # Recibe un modulo de texto y actualiza su contenido
def ActualizarTexto(ModuloTexto, nuevoTexto):
    ModuloTexto.value=nuevoTexto
    ModuloTexto.update()
    
    
    
    ###################################################################################
    ###################                   CASINO                    ###################
    ###################################################################################



    # Devuelve el puntaje de las cartas iniciales Y las cartas fisicas
def CasinoInicia(page):
    row_cartas_Casino = ft.Row(alignment=ft.MainAxisAlignment.CENTER)
    page.add(row_cartas_Casino)

    # Agregar cartas del inicio del Casino
    CartasCasino = Casino.CasinoInicia(row_cartas_Casino)
    
    return [CartasCasino, row_cartas_Casino]

    # Devuelve puntaje de la nueva carta
    # Se le puede pasar el Modulo de un texto mas su nuevo contenido para linkear la accion con la visualizacion del puntaje
def CasinoPideCarta(row_cartas_Casino, ModuloTexto = None, NuevoTexto = None):
    puntaje = Casino.PedirCarta(row_cartas_Casino, True)
    if ModuloTexto != None and NuevoTexto != None:
        NuevoTexto = NuevoTexto + f" {puntaje}"
        ModuloTexto.value = NuevoTexto
        ModuloTexto.update()
    
    
    # Da vuelta la carta del casino
def CasinoMuestraCarta():
    Casino.CierreApuestas()


    # Agrega un boton a la ventana que pide cartas a la mano del Casino
    # Si se le pasa un Modulo de texto y su nuevo contenido, actualizara ese texto y le agregara el nuevo puntaje
def AgregarBotonCasinoPideCarta(page, texto, row_cartas_Casino, ModuloTexto = None, NuevoTexto = None):
    if ModuloTexto != None and NuevoTexto != None:
        nuevoBoton = ft.ElevatedButton(text=texto, on_click=lambda _:CasinoPideCarta(row_cartas_Casino, ModuloTexto, NuevoTexto))
        page.add(nuevoBoton)
    else:
        nuevoBoton = ft.ElevatedButton(text=texto, on_click=lambda _:CasinoPideCarta(row_cartas_Casino))
        page.add(nuevoBoton)

    # Agrega un boton en la ventana que da vuelta la carta inicial del Casino        
def AgregarBotonCasinoMuestraCarta(page, texto):
    nuevoBoton = ft.ElevatedButton(text=texto, on_click=lambda _: CasinoMuestraCarta())
    page.add(nuevoBoton)
    

    ###################################################################################
    ###################                   JUGADOR                   ###################
    ###################################################################################

    # Crea la fila en la que iran los jugadores, se devuelve la fila para poder hacer cambios en los jugadores
def CrearInstanciaDeJugadores(page):
    row_jugadores = ft.Row(alignment=ft.MainAxisAlignment.CENTER, spacing=30)
    page.add(row_jugadores)
    return row_jugadores
    
    # Agrega un nuevo jugador a la lista de jugadores
def AgregarJugador(nombre, ip, jugadores):
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

    
    # Define la visibilidad de las cartas a otros jugadores
def JugadorVisibilidadCartas(Jugadores, ip_actual):
    for Jugador in Jugadores:
        if Jugador[1] == ip_actual:
            Jugador[3] = True
        else:
            Jugador[3] = False

    
    
    ###################################################################################
    ###################                 PROGRAMADOR                 ###################
    ###################################################################################

    # Codigo que contiene la logica del programa
def CodigoProgramador(page):
    Casino = CasinoInicia(page)
    print(f"CARTAS CASINO {Casino[0]}")

    
    AgregarTexto(page, "Genial esto funciona")
    CasinoPideCarta(Casino[1])
    puntaje = CalcularPuntaje(Casino[0])
    TextoPuntaje = AgregarTexto(page, f"Puntaje: {puntaje}")
    CasinoMuestraCarta()
    print(f"CARTAS CASINO: {Casino[0]}")
    
    puntaje = CalcularPuntaje(Casino[0])
    ActualizarTexto(TextoPuntaje, puntaje)
    
    AgregarBotonCasinoPideCarta(page, "PEDIR CARTA", Casino[1], TextoPuntaje, "Puntaje: ")
    
    row_jugadores = CrearInstanciaDeJugadores(page)
    
    ListaDeJugadores = []
    AgregarJugador("asd","192.168.0.1",ListaDeJugadores)
    AgregarJugador("SAD","192.168.0.11",ListaDeJugadores)
    print(ListaDeJugadores)
    
    JugadorInicia(ListaDeJugadores[0], row_jugadores,"192.168.0.1")
    JugadorInicia(ListaDeJugadores[1], row_jugadores,"192.168.0.1")

    print(f"LAS CARTAS DE {ListaDeJugadores[0][0]} son {ListaDeJugadores[0][2]}")
    
    
ft.app(IniciarVentana)