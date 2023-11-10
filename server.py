import socket
import threading

def handle_client(client_socket, target_host, target_port):
    target_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    target_socket.connect((target_host, target_port))

    while True:
        client_data = client_socket.recv(4096)
        if not client_data:
            break
        target_socket.send(client_data)

    while True:
        target_data = target_socket.recv(4096)
        if not target_data:
            break
        client_socket.send(target_data)

    client_socket.close()
    target_socket.close()

def start_proxy_server():
    proxy_host = '0.0.0.0'  # Listen on all available interfaces
    proxy_port = int(input("Enter the proxy server port (default: 8888): ") or 8888)
    target_host = input("Enter the target server host (e.g., www.example.com): ")
    target_port = int(input("Enter the target server port (e.g., 80): "))

    proxy_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxy_server.bind((proxy_host, proxy_port))
    proxy_server.listen(5)

    print(f'[*] Proxy server listening on {proxy_host}:{proxy_port}')

    while True:
        client_socket, addr = proxy_server.accept()
        print(f'[*] Accepted connection from {addr[0]}:{addr[1]}')

        client_handler = threading.Thread(
            target=handle_client,
            args=(client_socket, target_host, target_port)
        )
        client_handler.start()

if __name__ == '__main__':
    start_proxy_server()
