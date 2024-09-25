# main.py

import flet as ft
from BlackjackApp import BlackjackApp  # Importa la clase desde el archivo BlackjackApp.py

def main(page: ft.Page):
    # Crear una instancia de la clase BlackjackApp
    app = BlackjackApp()

    # Iniciar la ventana usando la clase
    app.iniciar_ventana(page)

# Iniciar la aplicación Flet
ft.app(target=main)
