#!/usr/bin/python

# 两个数组，元素个数为n，对应的是n位的二进制数，将它们相加，得出新的二进制数组
# 该程序用低字节存放的低位，高字节存放的高位
def add2Binaries(b1, b2, n):
    step = 0
    c = []

    for i in range(0, n):
        bit = b1[i] + b2[i] + step
        if bit >= 2:
            step = 1
            c.append(bit - 2)
        else:
            step = 0
            c.append(bit)
    c.append(step)
    return c

if __name__ == "__main__":
    b1 = [1,1,1,1]
    b2 = [0,1,1,1]
    c = add2Binaries(b1, b2, 4)
    print c
