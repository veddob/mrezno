#port_skener.py
import socket
import datetime

print("Program se izvodi na ovom racunalu: ")

print(datetime.datetime.now())

from local_machine_info import print_machine_info

print_machine_info()

print("----------------")

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

target=input("Molim vas unesite adresu hosta koju zelite testirati: ")

print("Skeniram adresu: ",target)

print("Unesite od kojeg do kojeg porta zelite napraviti skeniranje?")

port1 = input("Pocetni port => ")
port2 = input("Zavrsni port => ")

port1 = int(port1)
port2 = int(port2)

def scanner(port):
    try:
        sock.connect((target,port))
        return True
    except:
        return False
for portNumber in range(port1,port2):
    print("Skeniram port", portNumber)
    if scanner(portNumber):
        print('Port: ',portNumber,'/tcp',' je otvoren.')
print("Skeniranje porta zavrseno")
