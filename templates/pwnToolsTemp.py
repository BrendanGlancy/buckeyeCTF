# Pwntools template for brute forcing CTF challenges

from pwn import *

# Global variables
###############################################################

TARGET =  remote('misc.chall.pwnoh.io',13371)
PORT = args['RPORT'] or 1337
BINARY = args['BINARY'] or './binary'
LIBC = args['LIBC'] or './libc.so.6'
GDB = args['GDB'] or False
DEBUG = args['DEBUG'] or False

###############################################################

# Connection
###############################################################

r = remote(HOST, PORT)
resp = r.recvline()

###############################################################

# Functions
###############################################################
def start():
    if args['REMOTE']:
        return remote(HOST, PORT)
    else:
        return process(BINARY, env={'LD_PRELOAD': LIBC})

def debug():
    if args['GDB']:
        gdb.attach(r, """set follow-fork-mode child
        b *0x0000000000400B6A
        """)

def exploit():
    pass
###############################################################


# Main
###############################################################
def main():
    # prompt the user for input
    print("Enter the host IP address: ")
    HOST = input()
    print("Enter the port number: ")
    PORT = input()

    # see if their is a binary
    print("Is there a binary? (y/n): ")
    if input() == "y":
        print("Enter the binary name: ")
        BINARY = input()
        print("Is there a libc? (y/n): ")
        if input() == "y":
            print("Enter the libc name: ")
            LIBC = input()
        else:
            LIBC = ""
    else:
        BINARY = ""
        LIBC = ""

if __name__ == "__main__":
    main()

###############################################################
