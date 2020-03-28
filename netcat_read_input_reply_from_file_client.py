from pwn import *
from helpers import bytes_to_string

### start your netcat server: `netcat_read_input_reply_from_file_server.py`
### whatever you receive from there will be saved to the log file
### the content you send there will be saved to the log file with "INPUT: "
### the content to be sent is taken from `read_input_reply_from_file.txt`

with open('read_input_reply_from_file.txt', 'r') as f:
    content = f.readlines()

content = [x for x in content]

try:
    conn = remote('localhost', 4444)
    history = []

    for c in content:
        res = bytes_to_string(conn.recv())
        print(res)
        history.append(res)
    
        conn.send(c)
        history.append('INPUT: ' + c)

    res = bytes_to_string(conn.recv())
    print(res)
    history.append(res)

    conn.close()

except EOFError:
    pass

print(history)

with open('log_read_input_reply.txt', 'w') as f:
        for line in history:
            f.write(line)