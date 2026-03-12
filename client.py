import socket
# Create UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ("127.0.0.1", 15353)

# Get domain name from user
domain = input("Enter domain name: ")

# Send request to server
client_socket.sendto(domain.encode(), server_address)

# Receive response
ip_address, server = client_socket.recvfrom(1024)

print("IP Address:", ip_address.decode())

client_socket.close()