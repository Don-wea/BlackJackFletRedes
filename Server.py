import socket
import json
from BlackJack2 import BlackjackApp as BJ
import flet as ft

class ExecServer:
    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        print(f"Servidor escuchando en {self.host}:{self.port}")

        while True:
            client_socket, addr = self.server_socket.accept()
            print(f"Nueva conexión de {addr}")
            self.handle_client(client_socket)

    def handle_client(self, client_socket):
        try:
            while True:
                data = client_socket.recv(1024).decode('utf-8')
                if not data:
                    break
                if data == "REQUEST_CODE":
                    self.send_code(client_socket)
        except Exception as e:
            print(f"Error al manejar cliente: {e}")
        finally:
            client_socket.close()

    def send_code(self, client_socket):
        # Este es el código que se enviará al cliente para ser ejecutado
        f = open("code.py", "r")
        file = f.readlines()
        
        f.close()
        codigo = ""
        for line in file:
            codigo = codigo + line
        print(codigo)
        code_to_send = codigo 
        response = {
            'action': 'execute_code',
            'code': code_to_send
        }
        client_socket.send(json.dumps(response).encode('utf-8'))

if __name__ == "__main__":
    server = ExecServer()
    server.start()