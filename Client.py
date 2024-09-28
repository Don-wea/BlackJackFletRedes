import socket
import json
from BlackJack2 import BlackjackApp as BJ
import flet as ft
class ExecClient:
    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.socket.connect((self.host, self.port))
        print(f"Conectado al servidor en {self.host}:{self.port}")

    def request_and_execute_code(self):
        try:
            self.socket.send("REQUEST_CODE".encode('utf-8'))
            data = self.socket.recv(1024).decode('utf-8')
            message = json.loads(data)
            
            if message['action'] == 'execute_code':
                print("Ejecutando código recibido del servidor:")
                print("-" * 40)
                exec(message['code'])
                print("-" * 40)
            else:
                print("Acción desconocida recibida del servidor")
        except Exception as e:
            print(f"Error al recibir o ejecutar código: {e}")

    def run(self):
        self.connect()
        while True:
            input("Presione Enter para solicitar y ejecutar código del servidor (o Ctrl+C para salir)")
            self.request_and_execute_code()

if __name__ == "__main__":
    client = ExecClient()
    client.run()