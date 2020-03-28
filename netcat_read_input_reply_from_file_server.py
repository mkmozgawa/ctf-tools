from pwn import *
from helpers import bytes_to_string

lines_to_send = ['first line\n', 'second line\n', 'third line\n']

try:
    l = listen(4444)
    svr = l.wait_for_connection()
    svr.send('hi! send me lines :3\n')

    for line in lines_to_send:
        res = bytes_to_string(svr.recv())
        print(res)
        svr.send(line)

    svr.close()

except EOFError as e:
    print(e)