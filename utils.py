import socket

class Utils:
    def get_current_ip_address():
        ip_address = socket.gethostbyname(socket.gethostname())
        return ip_address