import socket
import threading

host = '192.168.0.110'
port = 8948

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nickNames = []

def broadCast(msg):
    for client in clients:
        try:
            client.send(msg)
        except:
            clientToRemove = clients.index(client)
            clients.remove(client)
            nickName = nickNames[clientToRemove]
            nickNames.remove(nickName)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            nickName = nickNames[clients.index(client)]
            broadCast(f"{nickName} : {message.decode()}".encode('ascii'))
        except:
            client.close()
            break

def accept():
    while True:
        client, addr = server.accept()
        client.send("Please Set Your NickName:".encode('ascii'))
        nickName = client.recv(1024)
        print(f"{addr} connected to the server")
        broadCast(f"{nickName} joined the chat".encode('ascii'))
        clients.append(client)
        nickNames.append(nickName)
        threading.Thread(target=handle, args=(client,)).start()

print("Server Running at ", host)
accept()

    

