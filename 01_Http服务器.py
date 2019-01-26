import socket


def serve_client(new_socket: socket.socket):
    request = new_socket.recv(1024)
    print(request)

    responce = "HTTP/1.1 200 OK\r\n"
    responce += "\r\n"
    responce += "<h1>hahahahaha</h1>"
    new_socket.send(responce.encode("utf-8"))
    new_socket.close()


def main():
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2. 绑定
    tcp_server_socket.bind(("", 7897))
    # 3. 设置为监听
    tcp_server_socket.listen(128)


    # 4. 等待新客户
    while True:
        new_socket, client_addr = tcp_server_socket.accept()
        # 5. 为这个客户服务
        serve_client(new_socket)


if __name__ == "__main__":
    main()
