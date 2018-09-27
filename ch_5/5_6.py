def num_bits(n, m):
    diff = n ^ m
    count = 0
    while diff != 0:
        if diff & 1:
            count += 1
        diff = diff >> 1
    return count


if __name__ == "__main__":
    m = 0b111
    n = 0b100
    print(num_bits(n,m))