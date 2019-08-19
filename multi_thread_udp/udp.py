import socket
import threading

def recv_msg(upd_socket):
    while True:
        recv_data = upd_socket.recvfrom(1024)
        print(recv_data)

def send_msg(upd_socket):
    while True:
        send_data = input("Message:")
        udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))

def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    udp_socket.bind(("", 7890))

    dest_ip = input("Destination IP:")
    dest_port = input("Destination Port:")

    t_recv = threading.Thread(target=recv_msg, args(udp_socket,))
    t_send = threading.Thread(target=send_msg, args(udp_socket, dest_ip, dest_port))

    t_recv.start()
    t_send.start()

if __name__ == "__main__":
    main()
