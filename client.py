import socket
import threading

def terima_pesan(sock):
    while True:
        try:
            pesan = sock.recv(1024).decode()
            if not pesan:
                break
            print(pesan, end='')
        except:
            break

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 5555))

username_prompt = sock.recv(1024).decode()
username = input(username_prompt)
sock.sendall(username.encode())

threading.Thread(target=terima_pesan, args=(sock,), daemon=True).start()

while True:
    pesan = input()
    if not pesan:
        continue
    sock.sendall(pesan.encode())
