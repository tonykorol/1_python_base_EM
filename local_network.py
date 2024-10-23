class Router:
    def __init__(self):
        self.buffer = []
        self.servers = []

    def link(self, server: "Server"):
        self.servers.append(server)
        server.router = self

    def unlink(self, server: "Server"):
        self.servers.remove(server)
        server.router = None

    def send_data(self):
        for data in self.buffer:
            server = self.get_server_by_ip(data[1])
            server.buffer.append(data)
        self.buffer.clear()

    def get_server_by_ip(self, ip: int):
        for server in self.servers:
            if server.ip == ip:
                return server


class Server:
    last_ip: int = 0

    def __init__(self):
        self.buffer = []
        self.ip = self.create_ip()
        self.router = None

    @classmethod
    def create_ip(cls):
        cls.last_ip += 1
        return cls.last_ip

    def __repr__(self):
        return f"Server {self.ip}"

    def send_data(self, data: "Data"):
        self.router.buffer.append(data)

    def get_ip(self):
        return self.ip

    def get_data(self):
        data = self.buffer.copy()
        self.buffer.clear()
        return data


class Data:
    def __init__(self, data: str, ip: int):
        self.data = data
        self.ip = ip
