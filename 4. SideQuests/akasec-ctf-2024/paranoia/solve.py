from pwn import *
from ctypes import CDLL
import time

if __name__ == "__main__":
    libc = CDLL("libc.so.6")  #truy cập vào C bằng hàm CDLL
    r = remote("20.80.240.190", 1234)
    current = int(time.time()) #lấy seed
    ct = list(map(int, r.recvline().strip().split(b" ")))
    libc.srand(current)
    for i in range(20):
        flag = b""
        for tmp in ct:
            v5 = libc.rand()
            flag += bytes([tmp ^ (v5 & 0xff)])
        print(flag)
    r.interactive()