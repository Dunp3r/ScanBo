import socket
from colorama import init, Fore, Back, Style
import threading

img = """
 ================================================
  ____                           ____          
 / ___|    ___    __ _   _ __   | __ )    ___  
 \___ \   / __|  / _` | | '_ \  |  _ \   / _ \ 
  ___) | | (__  | (_| | | | | | | |_) | | (_) |
 |____/   \___|  \__,_| |_| |_| |____/   \___/                                                 
 ================================================
 Created by Douglas Morean (aka. D0gp3r)
"""
init()
print(Fore.RED + img + Fore.RESET)
print()

ip = input(Style.BRIGHT+"ENTER THE IP ADDRESS TO SCAN: ")

port_comun = [
    21, 22, 23, 25, 53, 80, 110, 119, 123, 143, 161, 194, 443, 465, 514, 587, 993, 995, 1080, 1433, 1521, 3389, 5432, 5900, 6379,
    111, 135, 137, 138, 139, 161, 389, 445, 512, 513, 514, 1521, 2049, 2082, 2077, 2078, 2095, 2096, 3306, 3389, 5432, 5900, 5984, 6379, 7001, 7002, 8000,
    8080, 8443, 8888, 9092, 9200, 9300, 11211, 27017, 27018, 50070, 50030, 50060, 50075, 50090, 50105, 50470, 50475, 21000, 21212,
    22222, 27000, 27001, 27002, 27003, 27004, 27005, 27006, 27007, 27008, 27009, 27010, 27011, 27012, 27013, 27014, 27015, 27016,
    27017, 27018, 27019, 27020, 28017, 50030, 50070, 50075, 50090, 50105, 50470, 50475, 60010, 60030, 7077, 7078, 7199, 8765,
    10000, 12345, 16992, 16993, 27042, 34448, 38080, 38081
]

# LOOP MOST COMMON PORTS


def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Wait time in seconds
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(Fore.GREEN+f"[+] Port {port}: Open")
        sock.close()
    except KeyboardInterrupt:
        exit()
    except:
        pass


# Parallel port scanning using threads
threads = []
for port in port_comun:
    thread = threading.Thread(target=scan_port, args=(port,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
