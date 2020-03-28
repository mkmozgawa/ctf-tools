from pwn import *

l = listen(4444)
svr = l.wait_for_connection()
svr.send('hi\n')
svr.send('hello\n')