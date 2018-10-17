def generate_permutations(symbols):
    answer = []
    gen_perm(symbols, [[]], answer)
    return answer


def gen_perm(symbols, prefix, answer):
    if not symbols:
        answer.extend(prefix)
        return
    for s in symbols:
        copy_s = symbols.copy()
        copy_s.remove(s)
        new_prefixes = [[s] + x for x in prefix]
        gen_perm(copy_s, new_prefixes, answer)


def a(l):
    l.append([1])
    return

if __name__ == "__main__":
        ll = generate_permutations([1,2,3, 4])
        # print(len(l))
        l = [2]
        a(l)
        print(l)
