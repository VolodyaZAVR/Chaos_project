from Socket import Socket


class Server(Socket):
    def __init__(self):
        super(Server, self).__init__()
        self.bind(("localhost", 9999))
        self.listen(5)

    def set_up(self, connection="localhost"):
        self.bind((connection, 9999))

    def send_file(self, file_name=None):
        pass

    def listen_connection(self, user_connection=None):
        with open("filename.txt", "wb") as outfile:
            while True:
                data = user_connection.recv(1024)
                if not data:
                    print(f"End of receiving file {outfile}.")
                    break
                outfile.write(data)

    def start_server(self):
        while True:
            connection, address = self.accept()
            print("Connected: ", address)

            self.listen_connection(connection)

            connection.close()
            print("Connection was closed")


if __name__ == "__main__":
    server = Server()
    server.start_server()
