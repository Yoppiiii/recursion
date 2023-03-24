import socket
import sys
import os

def main():

    sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

    server_address = './local_socket_file'
    address = './local_client_socket_file'
    message = sys.stdin.buffer.readline()

    try:
        # アドレスの紐付けを解除する
        os.unlink(address)
    except FileNotFoundError:
        pass

    # クライアントのアドレスを紐付
    sock.bind(address)

    try:
        # データを送信
        print('sending {!r}'.format(message))
        sent = sock.sendto(message, server_address)

        # 応答を受信
        print('waiting to receive')
        data, server = sock.recvfrom(4096)
        print('received {!r}'.format(data))
        print('{}'.format(server))

    finally:
        print('closing socket')
        sock.close()

if __name__ == "__main__":
    main()