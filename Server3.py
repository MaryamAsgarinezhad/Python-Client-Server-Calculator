from datetime import datetime
from socket import *
serverPort= 12000
serverSocket= socket(AF_INET,SOCK_STREAM)
ADDR=("127.0.0.1",serverPort)
serverSocket.bind(ADDR)
serverSocket.listen(10)
print("The server is ready to receive")

a=0
b=0
number=0

while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    if sentence=="start":
        reply="OK"
        connectionSocket.send(reply.encode())

        # log
        start = datetime.now()
        print("      ", start.strftime("%H:%M:%S:%f")[:-4], " sending OK response to port 12000")

    else:
        if sentence == "exit":
            reply = "finished"
            print("finished!")
            connectionSocket.send(reply.encode())

            # log
            start = datetime.now()
            print("      ", start.strftime("%H:%M:%S:%f")[:-4], " sending finished response to port 12000")


            connectionSocket.close()
            break
        else:
            if sentence=="+" or sentence=="/" or sentence=="-" or sentence=="*" or sentence=="^":
                if sentence=="+":
                    ans=a+b
                if sentence=="-":
                    ans=a-b
                if sentence=="*":
                    ans=a*b
                if sentence=="/":
                    ans=a/b
                if sentence=="^":
                    ans=a**b

                connectionSocket.send(str(ans).encode())

                # log
                start = datetime.now()
                print("      ", start.strftime("%H:%M:%S:%f")[:-4], " sending answer calculated to port 12000")

            else:
                if sentence.isnumeric()==True:
                    number+=1
                    if number==1:
                        a=int(sentence)
                    if number==2:
                        b=int(sentence)
                        number=0
