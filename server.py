# server_udp.py

import socket

host = '127.0.0.1'
port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((host, port))

print(f"Server listening on {host}:{port}")

while True:
    data, client_address = server_socket.recvfrom(1024)
    marks_data = data.decode('utf-8').split(',')

    if len(marks_data) == 3:
        physics_marks = float(marks_data[0])
        chemistry_marks = float(marks_data[1])
        math_marks = float(marks_data[2])

        # Calculate the cutoff as the average of the sum of physics and chemistry marks and math marks
        cutoff = (physics_marks + chemistry_marks) / 2 + math_marks

        server_socket.sendto(str(cutoff).encode('utf-8'), client_address)
    else:
        server_socket.sendto("Invalid input".encode('utf-8'), client_address)
