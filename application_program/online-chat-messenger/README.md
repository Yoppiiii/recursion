# Online Chat Messenger

## Run
### server.py
```bash
❯ python3 server.py
❯ Serving on ('0.0.0.0', 12345)
```

### client.py
```bash
❯ python3 client.py
❯ 1. Create a room
❯ 2. Join a room
❯ 3. Send a message
❯ q. quit
```

## 1. Create a room
### client.py
```bash
❯ Enter your choice: 1
❯ Enter room name: new room
❯ Enter max room size: 3
❯ Enter room title: test
❯ 'Room created and joined'
```

### server.py
```bash
❯ host created new chatroom
❯ room key: 127.0.0.1:49838
❯ roomname: new room
❯ max room size: 3
❯ room title: test
❯ host: 127.0.0.1:51121
```

## 2. Join a room
### client.py
```bash
❯ Enter your choice: 2
❯ Enter room name: new room
❯ Enter your username: a
❯ (b'You are joined the new room', ('127.0.0.1', 12346))
```

### server.py
```bash
❯ a joined the new room
```


## 3. Send a message
### client.py
```bash
❯ Enter your choice: 3
❯ Enter room name: new room
❯ Enter your message: hello
❯ who do you send it to?: a
❯ (b'Roomname:new room, Msg_Size:5, Message:hello', ('127.0.0.1', 12346))
```

### server.py
```bash
❯ Recived a message from b
❯ To:a
❯ Message:hello
```
