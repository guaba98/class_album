import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET = IP, SPOK_STREAM = TCP

client.connect(('localhost', 1002))  # 127.0.0.1(ip 번호) / port(포트번호)

file = open('test.jpg', 'rb')
image_data = file.read(2048)

while image_data:
    client.send(image_data)
    image_data = file.read(2048)

file.close()
client.close()