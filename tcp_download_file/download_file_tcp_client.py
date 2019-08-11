import socket

def main():
    # 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 获取服务器的ip，port
    dest_ip = input("请输入下载服务器的ip: ")
    dest_port = int(input("请输入下载服务器的port: "))

    # 连接服务器
    tcp_socket.connect((dest_ip, dest_port))

    # 获取下载的文件名字
    download_filename = input("请输入要下载的文件名字: ")

    # 将文件名字发送到服务器
    tcp_socket.send(download_filename.encode("utf-8"))

    # 接收文件中的数据
    recv_data = tcp_socket.recv(1024) # 1k, 如果要下载大文件的话会更加复杂

    if recv_data:
        # 保存接收到的数据到一个文件中
        with open("[附件]" + download_filename, "wb") as f:
            f.write(recv_data)

    # 关闭套接字
    tcp_socket.close()

if __name__  == "__main__":
    main()
