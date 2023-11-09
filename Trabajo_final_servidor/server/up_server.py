import socketserver


class MyUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data, _ = self.request[0].strip(), self.client_address

        # Imprime el contenido del archivo recibido
        print("Contenido del archivo recibido:")
        print(data.decode("utf-8"))


if __name__ == "__main__":
    HOST, PORT = "localhost", 9995
    with socketserver.UDPServer((HOST, PORT), MyUDPHandler) as server:
        server.serve_forever()
