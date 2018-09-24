from ch_5 import get_binary_code

not_mask = 0b11111111111111111111111111111111

def insert(n, m, j, i):
    diff_mask = 2 ** (j+1) - 2 ** i
    not_diff_mask = diff_mask ^ not_mask
    print('{:032b}'.format(not_diff_mask))
    n_cleared = n & not_diff_mask
    print('{:032b}'.format(n_cleared))
    shifted_m = m << i
    return n_cleared | shifted_m
    # print(get_binary_code(all_ones))


if __name__ == "__main__":
    n = 0b01111111111111111111111111110101
    m = 0b101
    insert(n,m,3,1)
