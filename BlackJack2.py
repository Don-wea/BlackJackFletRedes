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
    
    def crear_texto(self, texto):
        modulo = ft.Text(value=texto, size=20)
        return modulo
    
        # Agrega un elemento en vertical al jugador
    def agregar_elemento_visual_jugador(self, jugador, elemento):
        jugador.controls.append(elemento)
        self.page.update()
        
        # Devuelve el puntaje de las cartas iniciales Y las cartas fisicas
    def casino_inicia(self):
        row_cartas_casino = ft.Row(alignment=ft.MainAxisAlignment.CENTER)
        self.page.add(row_cartas_casino)

        # Agregar cartas del casino
        cartas_casino = Casino.CasinoInicia(row_cartas_casino)
        return [cartas_casino, row_cartas_casino]
    
        # Se le puede pasar el Modulo de un texto mas su nuevo contenido para linkear la accion con la visualizacion del puntaje
    def casino_pide_carta(self, row_cartas_Casino, ModuloTexto = None, NuevoTexto = None):
        puntaje = Casino.PedirCarta(row_cartas_Casino, True)
        if ModuloTexto != None and NuevoTexto != None:
            NuevoTexto = NuevoTexto + f" {puntaje}"
            ModuloTexto.value = NuevoTexto
            ModuloTexto.update()
            
        # Da vuelta la carta del casino
    def casino_muestra_carta(self, ModuloTexto, NuevoTexto):
        cartas = Casino.CierreApuestas()
        NuevoTexto = NuevoTexto + str(self.calcular_puntaje(cartas))
        self.actualizar_texto(ModuloTexto, NuevoTexto)
        
        # Agrega un boton a la ventana que pide cartas a la mano del Casino
        # Si se le pasa un Modulo de texto y su nuevo contenido, actualizara ese texto y le agregara el nuevo puntaje
    def agregar_boton_casino_pide_carta(self, texto, row_cartas_Casino, ModuloTexto = None, NuevoTexto = None):
        if ModuloTexto != None and NuevoTexto != None:
            nuevoBoton = ft.ElevatedButton(text=texto, on_click=lambda _:self.casino_pide_carta(row_cartas_Casino, ModuloTexto, NuevoTexto))
            self.page.add(nuevoBoton)
        else:
            nuevoBoton = ft.ElevatedButton(text=texto, on_click=lambda _:self.casino_pide_carta(row_cartas_Casino))
            self.page.add(nuevoBoton)
            
            # Agrega un boton en la ventana que da vuelta la carta inicial del Casino        
    def agregar_boton_casino_muestra_carta(self, texto, ModuloTexto, NuevoTexto):
        nuevoBoton = ft.ElevatedButton(text=texto, on_click=lambda _: self.casino_muestra_carta(ModuloTexto,NuevoTexto))
        self.page.add(nuevoBoton)
        
        # Crea la fila en la que iran los jugadores, se devuelve la fila para poder hacer cambios en los jugadores
    def crear_instancia_de_jugadores(self):
        row_jugadores = ft.Row(alignment=ft.MainAxisAlignment.CENTER, spacing=30)
        self.page.add(row_jugadores)
        return row_jugadores
    
        # Agrega un nuevo jugador a la lista de jugadores
    def agregar_jugador(self, nombre, ip, jugadores):
        nuevoJugador = [nombre, ip]
        jugadores.append(nuevoJugador)
        
        # Devuelve el saldo actual del jugador
    def obtener_saldo_jugador(self, jugador):
        return jugador[3]
        
    def modificar_saldo_jugador(self, jugador, nuevo_monto):
        jugador[3] = nuevo_monto
        # Inicializa el jugador, dandole atributos y cartas. Se define su saldo inicial  
    def jugador_inicia(self, Jugador, row_jugadores):
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

        # IDEA DESCARTADA
        # Si el jugador es el mismo que la ip entonces retorna True
        #mostrar_cartas = Jugador[1] == ip_actual
        mostrar_cartas = True

        CartasJugador = []
        Saldo = 0
        Player.PedirCarta(row_cartas_Player, mostrar_cartas, CartasJugador)
        Player.PedirCarta(row_cartas_Player, mostrar_cartas, CartasJugador)
        Jugador.append(CartasJugador)
        Jugador.append(Saldo)
        print(f"Cartas actuales del jugador: {Jugador}")
        
        return [columna_jugador, row_cartas_Player]
    
        # Se le da una carta al jugador y actualiza su puntaje
    def jugador_pide_carta(self, Jugador, row_cartas_Player, TextoPuntaje, NuevoTexto):
        Player.PedirCarta(row_cartas_Player, True, Jugador[2])
        NuevoTexto = NuevoTexto + str(self.calcular_puntaje(Jugador[2]))
        self.actualizar_texto(TextoPuntaje, NuevoTexto)
    
        # Agrega un botón que permite a los jugadores pedir cartas
    def agregar_boton_jugador_pide_carta(self, texto, jugador, row_cartas_Player, ModuloTexto, NuevoTexto):
        nuevoBoton = ft.ElevatedButton(text=texto, on_click=lambda _:self.jugador_pide_carta(jugador, row_cartas_Player, ModuloTexto, NuevoTexto))
        self.page.add(nuevoBoton)

            
    # Método para ingresar la apuesta
    def agregar_apuesta(self, jugador, texto_saldo):
        apuesta_field = ft.TextField(label="Ingrese su apuesta", width=150)

        def confirmar_apuesta(e):
            apuesta = int(apuesta_field.value)
            saldo_actual = self.obtener_saldo_jugador(jugador)
            
            if apuesta <= saldo_actual:
                nuevo_saldo = saldo_actual - apuesta
                self.modificar_saldo_jugador(jugador, nuevo_saldo)
                self.actualizar_texto(texto_saldo, f"Saldo: {nuevo_saldo}")
            else:
                self.agregar_texto("Saldo insuficiente para esta apuesta")

        btn_apostar = ft.ElevatedButton(text="Confirmar Apuesta", on_click=confirmar_apuesta)

        self.page.add(ft.Row([apuesta_field, btn_apostar], alignment=ft.MainAxisAlignment.CENTER))
        self.page.update()
        
