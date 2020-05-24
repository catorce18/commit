import socket

HOST = 'localhost'
PORT = 2046
mensaje = "No soy el cliente"
s_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s_udp.sendto(mensaje.encode(), (HOST, PORT))

s_udp.close()
