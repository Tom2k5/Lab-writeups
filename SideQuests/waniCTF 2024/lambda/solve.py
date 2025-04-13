enc_flag = "16_10_13_x_6t_4_1o_9_1j_7_9_1j_1o_3_6_c_1o_6r"
a = list(enc_flag.split("_"))
flag = "".join(chr(int(c, 36) + 10) for c in a)
flag = "".join(chr(123 ^ ord(c)) for c in flag)
flag = "".join((chr(ord(c) + 3) for c in flag))
flag = "".join(chr(ord(c) - 12) for c in flag)
print(flag)

    