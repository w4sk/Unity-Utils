import socket

def receive_udp_packet(host='localhost', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind((host, port))
        print(f"Listening for UDP packets on {host}:{port}")
        while True:
            data, addr = sock.recvfrom(1024)
            print(f"Received message: {data.decode()} from {addr}")

receive_udp_packet()