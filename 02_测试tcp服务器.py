import socket


def client_serve(new_socket: socket.socket):
    rcv_content = new_socket.recv(1024)
    print(rcv_content)

    send_content = "HTTP/1.1 200 OK\r\n"
    send_content += "\r\n"
    send_content += "<h1>hah....ahah</h1>"
    new_socket.send(send_content.encode("utf-8"))
    new_socket.close()


def main():
    # 1. 建立套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    tcp_server_socket.bind(("", 7897))
    # 3. 设置为监听状态
    tcp_server_socket.listen(128)
    # 4. 为这个用户服务
    while True:
        new_socket, addr_info = tcp_server_socket.accept()
        client_serve(new_socket)


if __name__ == "__main__":
    main()
