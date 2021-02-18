import socket


class Socket(socket.socket):
    def __init__(self):
        super(Socket, self).__init__(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

    def set_up(self, connection="localhost"):
        raise NotImplementedError()

    def send_file(self, file_name=None):
        raise NotImplementedError()

    def listen_connection(self, user_connection=None):
        raise NotImplementedError()

    def start_server(self):
        raise NotImplementedError()
