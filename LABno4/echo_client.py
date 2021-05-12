import socket
import datetime
print(datetime.datetime.now())

from local_machine_info import print_machine_info

print_machine_info()

host = socket.gethostname()
port = 12345
client_socket = socket.socket()

client_socket.connect((host,port))

client_socket.sendall('HI'.encode())

while True:
    try:
        unos = input("Unesite neku recenicu: ")
        if unos == 'Nekarecenica':
        	raise ValueError
    except ValueError:
        print("Nedopušten unos!")
    else:
        break

print(unos)
#data = client_socket.recv(1024)

#print(data)
client_socket.close()