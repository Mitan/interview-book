def get_next_int(n):
    one_index = find_symbol(n, 0, 1)
    zero_index = find_symbol(n, one_index, 0)
    n = update_bit(n, 1, zero_index)
    num_ones = count_ones(n, zero_index)
    clear_mask = ~ (2 ** zero_index - 1)
    return (n & clear_mask) + 2 ** num_ones - 1


def count_ones(n, max_index):
    count = 0
    for i in range(max_index):
        if get_value_at_index(n, i) == 1:
            count += 1
    return count


def get_value_at_index(n, index):
    mask = 1 << index
    return 1 if n & mask != 0 else 0


# find first occurrence of symbol
def find_symbol(n, start_index, symbol):
    while get_value_at_index(n, start_index) != symbol and start_index < 32:
        start_index += 1
    if start_index == 32:
        raise Exception("NUM")
    return start_index


def clear_bit(n, ind):
    mask = ~(1 << ind)
    return mask & n


def update_bit(n, val, ind):
    cleared_n = clear_bit(n, ind)
    mask = val << ind
    return cleared_n | mask


if __name__ == "__main__":
    n = 0b100011110
    ans = get_next_int(n)
    print(bin(ans))