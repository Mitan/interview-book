def swap_bits(n):
    even_mask = 0xAAAAAAAA
    even_numbers = n & even_mask
    # no >>> in python
    odd_mask = (even_mask << 1) + 1
    # print(bin(odd_mask))
    odd_numbers = n & odd_mask
    # should be logical right shift
    return (odd_numbers << 1) + (even_numbers >> 1)


if __name__ == "__main__":
    n = 0b1011
    ans = swap_bits(n)
    print(bin(ans))