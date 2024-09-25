# BlackjackApp.py

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

        # Iniciar el código customizado
        self.codigo_programador()

    def calcular_puntaje(self, cartas):
        return Shuffle.CalcularPuntaje(cartas)

    def agregar_texto(self, texto):
        mensaje_texto = ft.Text(value=texto, size=20)
        self.page.add(mensaje_texto)
        return mensaje_texto

    def actualizar_texto(self, modulo_texto, nuevo_texto):
        modulo_texto.value = nuevo_texto
        modulo_texto.update()

    # Métodos relacionados con el casino
    def casino_inicia(self):
        row_cartas_casino = ft.Row(alignment=ft.MainAxisAlignment.CENTER)
        self.page.add(row_cartas_casino)

        # Agregar cartas del casino
        cartas_casino = Casino.CasinoInicia(row_cartas_casino)
        return [cartas_casino, row_cartas_casino]

    # Método para inicializar el código personalizado del programador
    def codigo_programador(self):
        # Aquí iría el código personalizado que se quiere inyectar
        pass
