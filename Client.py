
nickName=input("Please Set Your NickName your Are Going To Use: ")

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((host,port))



def connect():
    while True:
        try:
           message=client.recv(1024)
           if message.decode()=="Please Set Your NickName:":
                client.send(nickName.encode('ascii'))
           else:
                print(message.decode())
        except:
            client.close()
            break

def sent():
    while True:
        try:
            message=input("Reply: ")
            client.send(message.encode('ascii'))
        except:
            client.close()
            break



connectThread=threading.Thread(target=connect).start()
sentThread=threading.Thread(target=sent).start()




