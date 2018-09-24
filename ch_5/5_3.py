
def find_max_ones(input_str):
    if not input_str:
        return 0
    max_value = 0
    l = len(input_str)
    previous_len = 0
    # check zeroes
    cur_ind = 0
    while cur_ind < l:
        one_start_index, zero_l = check_sequence(cur_ind, l, input_str, '0')

        if one_start_index >= l and zero_l > 0:
            max_value = max(max_value, previous_len + 1)
            break
        one_end, one_l = check_sequence(one_start_index, l, input_str, '1')
        if zero_l == 1:
            max_value = max(max_value, previous_len + one_l + 1)
        elif zero_l == 0:
            max_value = one_l
        else:
            max_value = max(max_value, previous_len + 1)
        previous_len = one_l
        cur_ind = one_end

    return max_value


def check_sequence(start_index, total_length, arr, symbol):
    seq_len = 0
    while start_index < total_length and arr[start_index] == symbol:
        seq_len += 1
        start_index += 1
    return start_index, seq_len


if __name__ == "__main__":
    st = "1100"
    print(find_max_ones(st))
