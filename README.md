# Python-Client-Server-Calculator

The program server has the role of a calculator and by taking two numbers and one operator from the client performs the desired operation 
on the numbers and sends the output to the client.
It implements both server and client applications and use TCP protocol to communicate between them. Server after execution
waits for the client to connect. After connecting to the server, the client can request the calculation by sending the "start" command
to the server. After receiving this message, the server sends the string "OK" to the client and waits for the client to enter the numbers.

After receiving "OK", the client sends two integers and an operator, each in one line, to the server. By receiving the desired numbers and operators, 
the server performs the calculations and sends the result to the client,And then the same cycle repeats itself.
At each step, if the client sends the "exit" string to the server, the server will terminate the connection.
The client program should be written in such a way that after connecting to the server, it takes input from the user in a loop and sends it to the server,
And print the data received from the server. The loop ends when the user enters "exit".
Also, if the user enters an illegal command at any stage, the server must send a string containing the appropriate error text to the client
slow down and return to the beginning of the loop. (wait for "start" or "exit" command).
