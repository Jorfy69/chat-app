import socket

class Server:
    def __init__(self):
        self.sock = socket.socket()
        self.sock.bind(("127.0.0.1",4444))
    def event_loop(self):
            # 5 is the backlog of msgs
        s = self.sock
        s.listen(5)
        
        print(f"Socket is listening: {s}")
        
        while True:
            
            con, addr = s.accept()
            print('Got connection from', addr)
            
            con.send(b'Thank you for connecting')
            
            con.close()