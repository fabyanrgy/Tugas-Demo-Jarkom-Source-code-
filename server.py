import socket
import threading

clients = {}

def handle_client(conn, addr):
    conn.sendall("Masukkan username: ".encode())
    username = conn.recv(1024).decode().strip()
    clients[conn] = username
    print(f"{username} terhubung")
    broadcast(f"{username} telah bergabung\n", conn)

    while True:
        try:
            pesan = conn.recv(1024).decode().strip()
            if not pesan:
                break
            broadcast(f"{username}: {pesan}\n", conn)
        except:
            break

    del clients[conn]
    conn.close()
    print(f"{username} keluar")
    broadcast(f"{username} telah keluar\n", None)

def broadcast(pesan, pengirim):
    for conn in clients:
        if conn is not pengirim:
            try:
                conn.sendall(pesan.encode())
            except:
                pass

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 5555))
server.listen()
print("Server berjalan di port 5555...")

while True:
    conn, addr = server.accept()
    threading.Thread(target=handle_client, args=(conn, addr)).start()
