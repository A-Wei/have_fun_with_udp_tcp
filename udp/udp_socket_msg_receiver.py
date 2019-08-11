import socket

def main():
	# 创建套接字
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	# 绑定本地信息
	local_addr = ("", 7788)
	udp_socket.bind(local_addr)
	
	while True:
		# 接受数据
		recv_data = udp_socket.recvfrom(1024)
		#recv_data这个变量存储的是一个元组(接收到的数据byte，(发送方的ip，port))
		recv_msg = recv_data[0] #存储接收方的数据
		send_addr = recv_data[1] #存储发送方的地址信息
		# 打印数据
		print("%s:%s" % (str(send_addr), recv_msg.decode('utf-8')))
	
	# 关闭套接字
	udp_socket.close()
	
if __name__ == '__main__':
	main()
