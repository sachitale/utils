def var_int(x):
    varint = list()
    i = x & (0xffffffff if x <= 2**32 else 0xffffffffffffffff)
    print("       {:b}".format(i))
    while i != 0:
        t = i & 0xff
        i = i >> 8
        print("t  =  >{:b}".format(t))
        print("i  = >>{:b}".format(i))
        msb_set = t > 127
        if i == 0:
            varint.append(t)
        else:
            varint.append(t | 0x80)  # ensure last bit is set
        i = i << 1 | msb_set
        print("i2 = >>{:b}".format(i))
    return varint


if __name__ == "__main__":
    v = var_int(-2)
    for b in v: print("{:}".format(b))
