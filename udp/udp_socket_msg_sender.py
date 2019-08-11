import socket

def main():
    # 创建一个udp套接字
    udp_socket =  socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定本地信息
    udp_socket.bind('', 7890) 

    while True:
	    # 输入数据
	    send_data = input("Please input: ")

	    # 退出
	    if send_data == 'exit':
	    	break

	    # 可以使用套接字收发数据
	    udp_socket.sendto(send_data.encode("utf-8"), ('192.168.1.105', 7788))

    # 关闭套接字
    udp_socket.close()

if __name__ == "__main__":
	main()
