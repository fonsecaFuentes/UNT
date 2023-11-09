import socket
from pathlib import Path


def send_data():
    HOST, PORT = "localhost", 9995

    # Nombre del archivo a enviar
    root = Path(__file__).resolve().parent
    file_path = root / 'decorator_txt' / 'log.txt'

    with open(file_path, 'rb') as file:
        file_contents = file.read()

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Enviar el contenido del archivo al servidor
    sock.sendto(file_contents, (HOST, PORT))

    print("Archivo enviado con éxito.")
