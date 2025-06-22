import socket
import time
import os
import sys

DB_HOST = os.getenv("DB_HOST", "db")
DB_PORT = int(os.getenv("DB_PORT", 3306))

for i in range(30):
    try:
        socket.create_connection((DB_HOST, DB_PORT), timeout=2)
        print("Base de datos lista")
        sys.exit(0)
    except Exception:
        print(f"Esperando base de datos ({i+1}/30)...")
        time.sleep(2)

print("No se pudo conectar a la base de datos")
sys.exit(1)
