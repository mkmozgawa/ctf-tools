from pwn import *
from helpers import bytes_to_string

### start your netcat server on port 4444: `nc -l 4444`
### whatever you receive from there will be saved to the log file

try:
    conn = remote('localhost', 4444)

    res_lines = []
    res = bytes_to_string(conn.recvline())

    while res!= '':
        print(res)
        res_lines.append(res)
        res = bytes_to_string(conn.recvline())

    conn.close()

except EOFError:
    pass

print(res_lines)

with open('log_read_input.txt', 'w') as f:
        for line in res_lines:
            f.write(line)