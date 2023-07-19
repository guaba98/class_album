import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET = IP, SPOK_STREAM = TCP

server.bind(('localhost', 1002))  # 127.0.0.1(ip 번호) / port(포트번호)
server.listen()

client_socket, client_address = server.accept()

file = open('recive_pingu.jpg', 'wb')  # 바이너리 형태로 이미지를 읽음
image_chunk = client_socket.recv(2048)  # stream based protocol

while image_chunk:
    file.write(image_chunk)
    image_chunk = client_socket.recv(2048)

# file.write()
file.close()  # 스트림 닫기
client_socket.close()  # 클라이언트 소켓 닫기
