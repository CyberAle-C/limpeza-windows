import os
import platform
import socket
import getpass
import shutil
from datetime import datetime


def tamanho_legivel(bytes):
    gb = bytes / (1024 ** 3)
    if gb >= 1:
        return f"{gb:.2f} GB"

    mb = bytes / (1024 ** 2)
    return f"{mb:.2f} MB"


print("=" * 45)
print("        RELATORIO DO COMPUTADOR")
print("=" * 45)

print(f"Data...............: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
print(f"Usuario............: {getpass.getuser()}")
print(f"Computador.........: {socket.gethostname()}")
print(f"Sistema............: {platform.system()} {platform.release()}")
print(f"Versao.............: {platform.version()}")
print(f"Arquitetura........: {platform.machine()}")
print(f"Processador........: {platform.processor()}")

print("\n========== DISCO ==========")

disco = shutil.disk_usage("C:\\")

print(f"Total..............: {tamanho_legivel(disco.total)}")
print(f"Usado..............: {tamanho_legivel(disco.used)}")
print(f"Livre..............: {tamanho_legivel(disco.free)}")

print("\n========== REDE ==========")

try:
    ip = socket.gethostbyname(socket.gethostname())
except:
    ip = "Nao encontrado"

print(f"Nome...............: {socket.gethostname()}")
print(f"IP.................: {ip}")

print("\n========== PASTAS ==========")

print(f"Desktop............: {os.path.expanduser('~/Desktop')}")
print(f"Documentos.........: {os.path.expanduser('~/Documents')}")
print(f"Downloads..........: {os.path.expanduser('~/Downloads')}")

print("\n========== STATUS ==========")
print("Relatorio gerado com sucesso!")

print("=" * 45)