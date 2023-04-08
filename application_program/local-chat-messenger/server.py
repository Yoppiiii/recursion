import socket
import os
from faker import Factory


def main():

    sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    server_address = './local_socket_file'

    try:
        # アドレスの紐付けを解除する
        os.unlink(server_address)
    except FileNotFoundError:
        pass

    print('starting up on {}'.format(server_address))
    sock.bind(server_address)

    while True:
        print('\nwaiting to receive message')
        data, address = sock.recvfrom(4096)

        print('received {} bytes from {}'.format(len(data), address))
        print(data)

        if data:
            if data == b'hello\n':
                reply = 'hello, how are you doing?'
            elif data == b'bye\n':
                reply = 'see you again'
            else:
                fake = Factory.create('en_US')
                reply = fake.text()

            sent = sock.sendto(reply.encode(), address)
            print('sent {!r} bytes back to {}'.format(sent, address))


if __name__ == "__main__":
    main()
