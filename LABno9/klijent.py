import socket
import ssl
import datetime
print("Program se izvodi na ovom racunalu:")
print(datetime.datetime.now())

from local_machine_info import print_machine_info

print_machine_info()
print("-----------")


from server import HOST as SERVER_HOST
from server import PORT as SERVER_PORT

HOST = "127.0.0.1"
PORT = 60002

klijent = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
klijent.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

klijent = ssl.wrap_socket(klijent, keyfile="key.pem", certfile="certifikat.pem")

if __name__ == "__main__":
    klijent.bind((HOST, PORT))
    klijent.connect((SERVER_HOST, SERVER_PORT))

    while True:
        from time import sleep

        klijent.send("Hello World!".encode("utf-8"))
        sleep(1)