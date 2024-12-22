class Data:
    def __init__(self, data: str, ip: int):
        self.data = data
        self.ip = ip


class Router:
    router_buffer = []

    def __init__(self):
        self.servers = []

    def link(self, server: object):
        if server not in self.servers:
            self.servers.append(server)

    def unlink(self, server: object):
        if server in self.servers:
            self.servers.remove(server)

    def send_data(self):
        while Router.router_buffer:
            data = Router.router_buffer.pop(0)
            for server in self.servers:
                if server.get_ip() == data.ip:
                    server.server_buffer.append(data)


class Server:
    __ip_total = 1

    def __init__(self):
        self.server_buffer = []
        self.ip = Server.__ip_total
        Server.__ip_total += 1

    @staticmethod
    def send_data(data: object):
        Router.router_buffer.append(data)

    def get_data(self):
        if self.server_buffer:
            received = self.server_buffer[:]
            self.server_buffer = []
            return received
        else:
            return []

    def get_ip(self):
        return self.ip