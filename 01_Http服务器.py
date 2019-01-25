import socket


def serve_client(new_socket: socket.socket):
    """
    为这个客户端返回数据
    """

    # 1. 接受浏览器的请求
    # /GET / HTTP1.1
    request = new_socket.recv(128)
    print(request)

    # 2. 返回http格式的数据
    # 2.1 准备给浏览器的数据 header
    responce = "HTTP/1.1 200 OK\r\n"
    responce += "\r\n"

    # 2.2 准备给浏览器的数据 body
    responce += "<h2>hahahahaha</h2>"
    print(responce)
    new_socket.send(responce.encode("utf-8"))
    print("---sent---")
    new_socket.close()


def main():
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2. 绑定
    tcp_server_socket.bind(("192.168.31.79", 7897))
    # 3. 设置为监听
    tcp_server_socket.listen(128)


    # 4. 等待新客户
    while True:
        new_socket, client_addr = tcp_server_socket.accept()
        # 5. 为这个客户服务
        serve_client(new_socket)


if __name__ == "__main__":
    main()
