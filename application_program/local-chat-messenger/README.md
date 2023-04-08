# local-chat-messenger

## Preparation
```bash
❯ python3 -m venv env
❯ source env/bin/activate
❯ pip install -r req.txt
```

## Run
```bash
❯ python3 server.py
```

```bash
❯ python3 client.py
```

#### When the client sends "hello", the server responds with "hello, how are you doing?".

```bash
❯ python3 client.py
❯ hello
❯ sending b'hello\n'
❯ waiting to receive
❯ received b'hello, how are you doing?'
❯ ./local_socket_file
❯ closing socket
```

```bash
❯ python3 server.py
❯ starting up on ./local_socket_file
❯ waiting to receive message
❯ received 6 bytes from ./local_client_socket_file
❯ b'hello\n'
❯ sent 25 bytes back to ./local_client_socket_file

❯ waiting to receive message
```

#### When the client sends "bye", the server responds with "see you again".
```bash
❯ python3 client.py
❯ bye
❯ sending b'bye\n'
❯ waiting to receive
❯ received b'hello, how are you doing?'
❯ ./local_socket_file
❯ closing socket
```

```bash
❯ python3 server.py
❯ starting up on ./local_socket_file
❯ waiting to receive message
❯ received 4 bytes from ./local_client_socket_file
❯ b'bye\n'
❯ sent 13 bytes back to ./local_client_socket_file

❯ waiting to receive message
```

#### If anything other than the above is sent, a random sentence will be returned.
```bash
❯ python3 client.py
❯ hi
❯ sending b'hi\n'
❯ waiting to receive
❯ received b'Industry strong traditional production score. Key sound involve lawyer instead success. Election within ready.'
❯ ./local_socket_file
❯ closing socket
```

```bash
❯ python3 server.py
❯ starting up on ./local_socket_file
❯ waiting to receive message
❯ received 3 bytes from ./local_client_socket_file
❯ b'hi\n'
❯ sent 110 bytes back to ./local_client_socket_file

❯ waiting to receive message
```
