import asyncio
import socket
from collections import namedtuple
from typing import Dict

ChatClient = namedtuple('ChatClient', ['address', 'port', 'name', 'extra_data'])
ChatRoom = namedtuple('ChatRoom', ['clients', 'size', 'title'])

class ChatServer:
    def __init__(self, tcp_port, udp_port):
        self.tcp_port = tcp_port
        self.udp_port = udp_port
        self.rooms: Dict[str, ChatRoom] = {}
        self.clients: Dict[str, ChatClient] = {}

    async def handle_tcp_client(self, reader, writer):
        data = await reader.read(100)
        message = data.decode()
        roomname, max_size, title = message.split(':')
        max_size = int(max_size)
        if roomname not in self.rooms:
            chatroom = ChatRoom({}, max_size, title)
            self.rooms[roomname] = chatroom
            addr, port = writer.get_extra_info('peername')
            #TCPのアドレスとポート番号
            room_key = f'{addr}:{port}'
            self.clients[room_key] = ChatClient(addr, port, 'host', None)
            print('host created new chatroom')
            #ルームの情報
            print('room key: {}'.format(room_key))
            print('roomname: {}'.format(roomname))
            print('max room size: {}'.format(max_size))
            print('room title: {}'.format(title))
            writer.write(b'Room created and joined')
        else:
            writer.write(b'Room already exists')
        await writer.drain()
        writer.close()

    async def handle_udp_client(self, data, addr):
        message = data.decode()
        roomname, cmd, *rest = message.split(':')
        #UDP（クライアント）のアドレスとポート番号
        client_key = f'{addr[0]}:{addr[1]}'
        if cmd == 'join host':
            print('host: {}'.format(client_key))
        elif cmd == 'join':
            if client_key not in self.clients:
                self.clients[client_key] = ChatClient(addr[0], addr[1], rest[0], None)
            elif client_key in self.clients:
                self.udp_socket.sendto(b'You are already in another chat room', addr)
            
            if not roomname in self.rooms:
                self.udp_socket.sendto(b'That room does not exist', addr)
            elif len(self.rooms[roomname].clients) >= self.rooms[roomname].size:
                self.udp_socket.sendto(b'The room is full', addr)
            else:
                self.rooms[roomname].clients[client_key] = self.clients[client_key]
                for client in self.rooms[roomname].clients.values():
                    if f'{addr[0]}:{addr[1]}' != f'{client.address}:{client.port}' or len(self.rooms[roomname].clients) == 1:
                        print(f'{rest[0]} joined the {roomname}')
                        self.udp_socket.sendto(f'You are joined the {roomname}'.encode(), addr)
        elif cmd == 'msg':
            if not roomname in self.rooms:
                self.udp_socket.sendto(b'That room does not exist', addr)
            elif not client_key in self.rooms[roomname].clients:
                self.udp_socket.sendto(b'Please join the chatroom', addr)
            else:
                recipient, msg_size, message = rest
                clientname = ''
                flag = False
                for key, user in self.clients.items():
                    if user.name == recipient:
                        flag = True
                    if user.port == addr[1]:
                        clientname = user.name

                if flag == True:
                    print(f'Recived a message from {clientname}')
                    print(f'To:{recipient}')
                    print(f'Message:{message}')
                    self.udp_socket.sendto(f'Roomname:{roomname}, Msg_Size:{msg_size}, Message:{message}'.encode(), addr)                
                else: 
                    self.udp_socket.sendto(f'{recipient} is not participating in the chat'.encode(), addr)
                       
    async def start(self):
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_socket.bind(('0.0.0.0', self.udp_port))
        loop = asyncio.get_running_loop()
        loop.add_reader(self.udp_socket, self.udp_reader)

        server = await asyncio.start_server(self.handle_tcp_client, '0.0.0.0', self.tcp_port)
        addr = server.sockets[0].getsockname()
        print(f'Serving on {addr}')

        async with server:
            await server.serve_forever()

    def udp_reader(self):
        data, addr = self.udp_socket.recvfrom(1024)
        asyncio.create_task(self.handle_udp_client(data, addr))

if __name__ == '__main__':
    server = ChatServer(tcp_port=12345, udp_port=12346)
    asyncio.run(server.start())