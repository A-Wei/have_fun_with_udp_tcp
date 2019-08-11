import socket


def main():
    # 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定ip和port
    tcp_server_socket.bind(('', 7878))

    # 让套接字变为被动连接
    tcp_server_socket.listen(128)

    # 等待客户端的连接, accept 返回一个元组(tuple), 由新创建的套接字来给客户端发送信息
    new_client_socket, client_addr = tcp_server_socket.accept()

    # 接收客户端发送过来的请求
    recv_data = new_client_socket.recv(1024)
    new_client_socket.send("ok".encode("utf-8"))

    # 关闭套接字
    tcp_server_socket.close()
    new_client_socket.close()


if __name__ == "__main__":
    main()
