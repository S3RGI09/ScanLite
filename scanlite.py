#!/usr/bin/python3


import sys
import socket


print()
print("\033[1;31m"+" ____   ____    _    _   _   _ _ _       ")
print("\033[1;31m"+"/ ___| / ___|  / \  | \ | | | (_) |_ ___ ")
print("\033[1;31m"+"\___ \| |     / _ \ |  \| | | | | __/ _ \  github.com/S3RGI09")
print("\033[1;31m"+" ___) | |___ / ___ \| |\  | | | | ||  __/")
print("\033[1;31m"+"|____/ \____/_/   \_\_| \_| |_|_|\__\___|  V1.5")
print()

print("\033[;36m"+"Herramienta creada por S3RGI09 (Sergio Casero Verdial)")
print("\033[;35m"+"*Si va a hacer pentest, auditorias o mantenimiento descarge Scan en mi GitHub")
print("\033[1;34m"+"----------------------------------------------------------------------------")
objetivo= socket.gethostbyname(input("\033[1;32m"+"Inserte la direccion IP: "))
print("\033[1;34m"+"------------------------------------------------------")

print("Escaneando objetivo: " + objetivo)

try:
        for port in range(1,150):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                resultado = s.connect_ex((objetivo, port))
                if resultado == 0:
                        print("Puerto {} abierto".format(port))
                s.close()
except:
        print("\n Saliendo...")
        sys.exit(0)
