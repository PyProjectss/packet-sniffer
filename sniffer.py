#importing socket layer to sniff INET
import socket

#INET raw socket packet
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)


#receiving packets from 65565, udp/tcp
while True:
  print(s.recvfrom(65565)) 
  