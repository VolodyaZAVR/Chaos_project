from Socket import Socket


class Client(Socket):
    def __init__(self):
        super(Client, self).__init__()

    def set_up(self, connection="localhost"):
        self.connect((connection, 9999))
        self.send_file("input1.jpg")

    def send_file(self, file_name=None):
        with open(file_name, "rb") as file:
            while True:
                # read 1024 bytes from file
                file_data = file.read(1024)
                # sending 1024 bytes to server
                self.send(file_data)
                if not file_data:
                    break
        print(f"File sent: {file_name}")

    def listen_connection(self, user_connection=None):
        pass

    def start_server(self):
        pass


if __name__ == "__main__":
    client = Client()
    client.set_up()
