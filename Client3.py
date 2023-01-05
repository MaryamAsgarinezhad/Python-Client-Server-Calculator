from datetime import datetime
from socket import *
serverName= "127.0.0.1"
serverPort= 12000

state=""
sentence=""
while True:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    if state=="n1":
        sentence = input("Input Number1:")
        if not (sentence.isnumeric()):
            print("Number1 you entered is not a numer")
            state = ""
            clientSocket.close()
            continue
        else:
            clientSocket.send(sentence.encode())

            # log
            start = datetime.now()
            print("      ", start.strftime("%H:%M:%S:%f")[:-4], " sending number1 to port 12000")

            state = "n2"
            clientSocket.close()
            continue

    if state=="n2":
        sentence = input("Input Number2:")
        if not (sentence.isnumeric()):
            print("Number2 you entered is not a numer")
            state = ""
            clientSocket.close()
            continue
        else:
            clientSocket.send(sentence.encode())

            # log
            start = datetime.now()
            print("      ", start.strftime("%H:%M:%S:%f")[:-4], " sending number2 to port 12000")

            state = "op"
            clientSocket.close()
            continue

    if state=="op":
        sentence = input("Input operation:")
        if not (ord(sentence) == 94 or ord(sentence) == 42 or ord(sentence) == 43 or ord(sentence) == 45 or ord(
                sentence) == 47):
            print("invalid operation")
            clientSocket.close()
            state = ""
            continue
        else:
            clientSocket.send(sentence.encode())

            # log
            start = datetime.now()
            print("      ", start.strftime("%H:%M:%S:%f")[:-4], " sending operator to port 12000")

            reply = clientSocket.recv(1024)
            print("From Server:", reply.decode())
            clientSocket.close()
            state = ""
            continue

    if state=="":
        sentence = input("Input sentence:")
        if not(sentence=="start" or sentence=="exit"):
            print("invalid sentence")
            clientSocket.close()
            continue

        clientSocket.send(sentence.encode())

        # log
        start = datetime.now()
        print("      ", start.strftime("%H:%M:%S:%f")[:-4], " sending sentence to port 12000")

        reply = clientSocket.recv(1024)
        print("From Server:", reply.decode())
        if reply.decode() == "OK":
            clientSocket.close()
            state = "n1"
            continue
        if reply.decode() == "finished":
            clientSocket.close()
            break
        if reply.decode() == "invalid sentence":
            clientSocket.close()
            continue
        clientSocket.close()