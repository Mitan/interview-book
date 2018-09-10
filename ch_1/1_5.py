import sys

def compare_insert(longer, shorter, shorter_len):
    differ = False
    shift = 0
    for i in range(shorter_len):
        if longer[i + shift] != shorter[shift]:
            if not differ:
                differ = True
                shift = 1
            else:
                return False
    return True


def compare_change(f, s, l):
    differ = False
    for i in range(l):
        if f[i] != s[i]:
            if not differ:
                differ = True
            else:
                return False
    return True


def check_strings(s_1, s_2, len_1, len_2):
    if abs(len_1 - len_2) > 1:
        return False
    elif len_1 == len_2 + 1:
        return compare_insert(s_1, s_2, len_2)
    elif len_2 == len_1 + 1:
        return compare_insert(s_2, s_1, len_1)
    else:
        return compare_change(s_1, s_2, len_1)


s_1 = list(sys.stdin.readline())
s_2 = list(sys.stdin.readline())
len_1 = len(s_1)
len_2 = len(s_2)
print(check_strings(s_1, s_2, len_1, len_2))

