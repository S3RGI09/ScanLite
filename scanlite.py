#!/usr/bin/python3


import sys
import socket


print()
print(" ____   ____    _    _   _   _ _ _       ")
print("/ ___| / ___|  / \  | \ | | | (_) |_ ___ ")
print("\___ \| |     / _ \ |  \| | | | | __/ _ \ ")
print(" ___) | |___ / ___ \| |\  | | | | ||  __/")
print("|____/ \____/_/   \_\_| \_| |_|_|\__\___|")
print()

print("Herramienta creada por S3RGI09 (Sergio Casero Verdial)")
print("Si va a hacer pentest, auditorias o mantenimiento descarge Scan en mi GitHub")
print("----------------------------------------------------------------------------")
objetivo= socket.gethostbyname(input("Inserte la direccion IP: "))
print("------------------------------------------------------")

print("Escaneando objetivo: " + objetivo)

try:
	for port in range(1,150):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		resultado = s.connect_ex((objetivo, port))
		if resultado == 0:
			print("El puerto {} está abierto".format(port))
		s.close()
except:
	print("\n Saliendo...")
	sys.exit(0)
