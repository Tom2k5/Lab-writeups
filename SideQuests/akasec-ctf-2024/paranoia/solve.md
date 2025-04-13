# Overview
- Paranoia là 1 dạng về `rand()`.
```
int __cdecl main(int argc, const char **argv, const char **envp)
{
  unsigned int v3; // eax
  int v4; // ebx
  int v5; // eax
  unsigned __int64 i; // [rsp+8h] [rbp-18h]

  v3 = time(0LL);
  srand(v3);
  for ( i = 0LL; i <= 17; ++i )
  {
    v4 = flag[i];
    v5 = rand();
    printf("%i ", v4 ^ ((unsigned __int8)(((unsigned int)(v5 >> 31) >> 24) + v5) - ((unsigned int)(v5 >> 31) >> 24)));
  }v5
  putchar(10);
  return 0;
}
```
- Đề cho 1 file `chall` và cổng kết nối `nc 20.80.240.190 1234`.
![Alt text](CTF-writeups/SideQuests/akasec-ctf-2024/Solution/image/image-3.png)
- Ta có thể thấy file in enc_flag.
- Đọc chương trình
=> `flag[i] ^ v5 = output` 
=> `flag[i] = output ^ v5`
# Solution
- Vì `rand()` trong C khác với python => dùng thư viện `ctype` để lấy hàm rand C.
=> Tham khảo cách dùng: *https://dev.to/petercour/call-dll-functions-from-python-jo4*
- Trước khi giải quyết bài toán này, ta phải bt 1 ít về pwntool để viết script.
=> Bạn có thể đọc web này: *https://nobinpegasus.github.io/blog/a-beginners-guide-to-pwntools*
```
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
```
- Đầu tiên ta import các thư viện.
- Tiếp theo thực hiện XOR từng kí tự rồi in ra là xong.
- Lưu ý: python3 chỉ cho phép đọc từ server dưới dạng bytes `b" "` cũng như lúc in flag ra.
![Alt text](CTF-writeups/SideQuests/waniCTF%202024/lambda/image.png)