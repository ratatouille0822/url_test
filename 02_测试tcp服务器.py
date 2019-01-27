import socket
import re


def client_serve(new_socket: socket.socket):
    print("=" * 50)
    rcv_content = new_socket.recv(1024).decode("utf-8")
    rcv_lines = rcv_content.splitlines()
    print(rcv_lines)
    # page = re.match(r"\s(\w+)(/(\w)+-(\w)+)*\.(\w){1,10}", rcv_lines[0]).group()
    page = re.match(r"[^/]+(/[^ ]*)", rcv_lines[0]).group(1)
    file_name = "./html" + page
    print(file_name)
    try:
        fp = open(file_name, "rb")
    except:
        send_content = "HTTP/1.1 200 OK\r\n"
        send_content += "\r\n"
        send_content += "----file not found----"
        new_socket.send(send_content.encode("utf-8"))
    else:
        html_content = fp.read()
        fp.close()
        send_content = "HTTP/1.1 200 OK\r\n"
        send_content += "\r\n"
        new_socket.send(send_content.encode("utf-8"))
        new_socket.send(html_content)
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
