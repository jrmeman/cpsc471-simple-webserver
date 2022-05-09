# Name: Justin Meman
# Due Date: 3/19/2021

#import socket module
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a server socket

# TASK 1
#Fill in start
serverPort = 45678
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('the web server is up on port: ', serverPort)
#Fill in end

while True:
   #Establish the connection
   print('Ready to serve...')

   # TASK 2
   connectionSocket, addr = serverSocket.accept()

   try:

      # TASK 3
      message = connectionSocket.recv(1024)

      filename = message.split()[1]
      f = open(filename[1:])

      # TASK 4
      outputdata = f.read()

      # TASK 5
      #Send one HTTP header line into socket
      #Fill in start
      connectionSocket.send(b"HTTP/1.1 200 OK \r\n\r\n")
      #Fill in end

      #Send the content of the requested file to the client
      for i in range(0, len(outputdata)):
         connectionSocket.send(outputdata[i].encode())
      connectionSocket.send("\r\n".encode())
      connectionSocket.close()
   except IOError:

      # TASK 6
      #Send response message for file not found
      #Fill in start
      connectionSocket.send(b"HTTP/1.1 404 Not Found\r\n\r\n")
      #Fill in end

      # TASK 7
      #Close client socket
      #Fill in start
      connectionSocket.close()
      #Fill in end

serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data
