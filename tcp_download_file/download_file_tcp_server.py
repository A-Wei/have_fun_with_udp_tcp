import socket


def send_file_to_client(new_client_socket, client_addr):
    # 接收客户端发送过来的 要下载的文件名
    filename = new_client_socket.recv(1024).decode("utf-8")
    print("客户端(%s)需要下载文件是：%s" % (str(client_addr), filename))

    file_content = None
    # 打开这个文件，读取数据, 如果新建文件的话，一般用with，如果是读的话，一般用try。
    # 因为如果新建的话，with一般不报错，但是读文件，with可能会报错，例如没有这个文件。
    try:
        f = open(filename, "rb")
        file_content = f.read()
        f.close()
    except Exception as ret:
        print("没有要下载的文件(%s)" % filename)

    # 发送文件的数据给客户端
    if file_content:
        new_client_socket.send(file_content)


def main():
    # 创建套接字 socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定本地信息 bind
    tcp_server_socket.bind(("", 7878))

    # 让默认的套接字由主动变为被动 listen
    tcp_server_socket.listen(128) #操作系统决定具体能有多少个同时连接，不一定128，但是数值越大，能连接的越多。

    while True:
        # 等待客户端的链接 accept
        new_client_socket, client_addr = tcp_server_socket.accept()

        # 调用发送文件函数，完成为客户端服务
        send_file_to_client(new_client_socket, client_addr)

        # 关闭套接字
        new_client_socket.close()

    tcp_server_socket.close()


if __name__ == "__main__":
    main()
