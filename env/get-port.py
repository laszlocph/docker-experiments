#http://unix.stackexchange.com/questions/55913/whats-the-easiest-way-to-find-an-unused-local-port

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 0))
addr = s.getsockname()
print addr[1]
s.close()

