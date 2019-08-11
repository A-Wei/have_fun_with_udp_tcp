import socket


def main():
    # 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定ip和port
    tcp_server_socket.bind(('', 7878))

    # 让套接字变为被动连接
    tcp_server_socket.listen(128)

    while True: # 循环为多个客户端服务
        print("等待新的客户端连接")
        # 等待客户端的连接, accept 返回一个元组(tuple), 由新创建的套接字来给客户端发送信息
        new_client_socket, client_addr = tcp_server_socket.accept()
        print("客户端已连接%s" % str(client_addr))

        while True: # 循环为一个客户端服务多次
            # 接收客户端发送过来的请求
            recv_data = new_client_socket.recv(1024)
            print("客户端发送过来的请求是:%s" % recv_data.decode("utf-8"))
            import ipdb; ipdb.set_trace()

            # 如果recv解堵塞，那么有2种方式，1客户端发送过来数据，2客户端调用close()导致recv接阻塞
            if recv_data:
                # 回送数据给客户端
                new_client_socket.send("ok".encode("utf-8"))
                recv_data = None
            else:
                break

        # 关闭accept返回的套接字，不会再为这个客户端服务
        new_client_socket.close()
        print("服务器关闭")

    # 如果将监听套接字关闭了，那么会导致不能再次等到新的客户端到来
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
