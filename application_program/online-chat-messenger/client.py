import socket

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def create_room():
    roomname = input('Enter room name: ')
    max_size = input('Enter max room size: ')
    title = input('Enter room title: ')
    message = f'{roomname}:{max_size}:{title}'
    tcp_socket.connect(('0.0.0.0', 12345))
    tcp_socket.sendall(message.encode())
    data = tcp_socket.recv(1024)
    print(repr(data.decode()))

    udp_socket.sendto(f'{roomname}:join host:host'.encode(), ('0.0.0.0', 12346))
    data, _ = udp_socket.recvfrom(1024)
    print(data.decode())
        
def join_room():
    roomname = input('Enter room name: ')
    username = input('Enter your username: ')
    udp_socket.sendto(f'{roomname}:join:{username}'.encode(), ('0.0.0.0', 12346))
    data = udp_socket.recvfrom(1024)
    print(repr(data))

def send_message():
    roomname = input('Enter room name: ')
    message = input('Enter your message: ')
    msg_size = len(message)
    recipient = input('who do you send it to?: ')
    udp_socket.sendto(f'{roomname}:msg:{recipient}:{msg_size}:{message}'.encode(), ('0.0.0.0', 12346))
    data = udp_socket.recvfrom(1024)
    print(repr(data))

if __name__ == '__main__':
    while True:
        print('1. Create a room')
        print('2. Join a room')
        print('3. Send a message')
        print('q. quit')
        choice = input('Enter your choice: ')
        
        if choice == '1':
            create_room()
        elif choice == '2':
            join_room()
        elif choice == '3':
            send_message()
        elif choice == 'q':
            break