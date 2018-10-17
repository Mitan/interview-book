def right_logical_shift(val, n):
    return val >> n if val >= 0 else (val + 0x100000000) >> n

def multiply(m,n):
    if m == 0 or n == 0:
        return 0
    # last digit
    d1 = m & 1
    d2 = n & 1
    # need logical shift but python doesn't have it
    r1 = right_logical_shift(m, 1)
    r2 = right_logical_shift(n, 1)
    ans = (d1 & d2) + (multiply(r1, r2) << 2)
    if d1:
        ans += r2 << 1
    if d2:
        ans += r1 << 1
    return ans


if __name__ == "__main__":
    n = 3
    m = 4
    print(multiply(4, 3))