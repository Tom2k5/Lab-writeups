enc_flag = [168,138,191,165,765,89,222,36,101,271,222,35,349,66,44,222,9,101,222,81,239,319,36,83,349,72,83,222,9,83,331,36,101,222,54,83,349,18,74,292,63,95,334,213,11]

for j in range(len(enc_flag)):
    for i in range(2, -1, -1):
        v4 = (j + i) % 3
        if v4 == 0:
            enc_flag[j] //= 3
        elif v4 == 1:
            enc_flag[j] -= 5
        elif v4 == 2:
            enc_flag[j] ^= 0x7f
for i in enc_flag:
    print(chr(i), end = "")
            