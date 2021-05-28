import socket
from multiprocessing import Pool
import time
import sys

openPorts = []  
scannedPorts = []

try:
    ip = sys.argv[1]
except IndexError:
    print("[!] Error: No IP Entered")
    print("\n[+] Syntax: python portscan.py IP")
    sys.exit()

def banner():
    """ Banner Message"""
    banner = """
=====================Port Scanner====================
    Multiprocessing Port Scanner and Banner Check    
=====================================================
Syntax: python portscan.py IP
e.g python portscan.py 192.168.1.8
    """
    return banner

def portScan(port):
    """ Checks open port"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)  
        pcheck = s.connect_ex((str(ip), port))
        if pcheck == 0: 
            openPorts.append(port) 
            return pcheck
        s.close() 
    except socket.error as e:
        pass

def bannerGrab(port):
    """ Retrieves Banner Message from Service if it exists"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5) 
        s.connect((str(ip), port)) 
        bann = s.recv(50)
        return bann 
    except socket.error as e:
        pass

def main(port):
    """ Runs the main script"""
    if portScan(port) == 0:
        print("[+] Port Open: %d" % port)
        if bannerGrab(port): 
            print("  [-] Port %d Banner: %s" % (port, str(bannerGrab(port))))
    else:
        pass

if __name__ == "__main__": 
    print(banner())
    tstart = time.time() 
    print("[+] Reading Ports from File")
    newPorts = range(1, 65536) 
    print("[+] Starting up the engines!\n")
    print("[+] Scanning IP Address: %s" % ip)
    print("[+] Scanning %d Ports" % len(newPorts))

    with Pool(processes=40) as pool:
        for i in pool.imap_unordered(main, [int(p) for p in newPorts]):
            if i:
                continue
            else:
                pass
    tend = time.time() - tstart
    print("\n[+] Finished in %d Seconds" % tend)