
# true_str = sys.stdin.readline()[:-1]
true_str = ' ll aaa bb c'
true_len = len(true_str)
input_str = list(true_str) + 10 * [' ']

num_spaces = 0
for i in range(true_len):
        if input_str[i] == ' ':
            num_spaces += 1

for i in range(true_len-1, -1, -1):
        if num_spaces == 0:
                break
        if input_str[i] != ' ':
                input_str[i + 2 * num_spaces] = input_str[i]
        else:
            input_str[i + 2 * num_spaces] = '0'
            input_str[i + 2 * num_spaces -1] = '2'
            input_str[i + 2 * num_spaces - 2] = '%'
            num_spaces -= 1

print(''.join(input_str))