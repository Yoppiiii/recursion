import json
import socketserver


def floor(x):
    return int(x)


def nroot(n, x):
    return x ** (1 / n)


def reverse(s):
    return s[::-1]


def validAnagram(s, t):
    return sorted(s) == sorted(t)


def sort(words):
    return sorted(words)


class RpcRequestHandler(socketserver.BaseRequestHandler):
    def setup(self):
        super().setup()
        self.request.settimeout(10)

    def handle(self):
        # Read JSON-RPC request from the client
        data = self.request.recv(1024).strip()
        request = json.loads(data.decode('utf-8'))
        print(request)

        # Extract method name and arguments from the request
        method = request['method']
        params = request['params']

        # Call the appropriate function with the given arguments
        if method == 'floor':
            result = floor(*map(float, params))
        elif method == 'nroot':
            result = nroot(*params)
        elif method == 'reverse':
            result = reverse(*params)
        elif method == 'validAnagram':
            result = validAnagram(*params)
        elif method == 'sort':
            result = sorted(params)
        else:
            result = {'error': 'Unknown method'}

        # Build the JSON-RPC response and send it back to the client
        response = {
            'result': result,
            'result_type': request['param_types'],
            'id': request['id']
        }
        self.request.sendall(json.dumps(response).encode('utf-8'))

    def teardown(self):
        super().teardown()
        self.request.close()


if __name__ == '__main__':
    # Set up a TCP server listening on localhost:8000
    with socketserver.TCPServer(('localhost', 8000), RpcRequestHandler) as server:
        print('Server is listening on port 8000...')
        server.serve_forever()
