import socket

target_host =  "www.google.com"
target_port = 80

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((target_host,target_port))

client.send("GET / HTTP/1.1\r\Host: google.com\r\n\r\n")

respone = client.recv(4096)
print(respone)
print("if this line is show up then your program fuck ")
