# client_udp.py

import socket

host = '127.0.0.1'
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

physics_marks = float(input("Enter Physics marks: "))
chemistry_marks = float(input("Enter Chemistry marks: "))
math_marks = float(input("Enter Math marks: "))

# Sending marks as a comma-separated string
marks_data = f"{physics_marks},{chemistry_marks},{math_marks}"
client_socket.sendto(marks_data.encode('utf-8'), (host, port))

data, _ = client_socket.recvfrom(1024)
result = data.decode('utf-8')

print(f"The cutoff is: {result}")
