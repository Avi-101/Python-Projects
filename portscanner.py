
import socket #communicate with other machines using TCP/UDP protocols


def scan(targets, ports):
	print('\n'+ 'Starting Scan for ' + str(targets))  #defines which target's results displayed
	for port in range(1, ports):  #calls scanport func from 1 to input num
		scan_port(targets, port)

def scan_port(ipadress,port): #scan port function taking ipadress and port as parameters 
	try:
		sock = socket.socket() #calling socket function from library 
		sock.connect((ipadress, port)) #can connect or not connect
		print("[+] Port Opened " + str(port)) #if connect, open port found, print # as str
		sock.close() #close after use
	except: 
		pass #if not connect, port is closed


targets = input("[*] Enter Targets to Scan (use a comma to seperate): ")   #user inputs target ip addresses
ports = int(input("[*] Enter Amount of Ports to Scan: "))     #user input number of ports to scan, converted to int

if ',' in targets:
	print("[*] Scanning Multiple Targets")  #notification of multiple targets as input
	for ip_addr in targets.split(','):  #split user input by comma
		scan(ip_addr.strip(' '), ports)  #scan multiple targets
else:
	scan(targets,ports)  #scan single target