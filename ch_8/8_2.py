def find_path_main(mines, r, c):
    if r == 0 or c == 0:
        raise Exception("wrong dimensions")
    memo = {(0, 0): True}
    ans = find_path(mines, (r - 1, c - 1), memo)
    print(memo)
    return ans


def find_path(mines, curr, memo):
        if curr in mines:
            return False, []
        if curr in memo.keys():
            return memo[curr], []

        c1, c2 = curr

        if c1 < 0 or c2 < 0:
                return False, []
        a1, p1 = find_path(mines, (c1 - 1, c2), memo)
        a2, p2 = find_path(mines, (c1, c2 - 1), memo)
        a = a1 or a2
        memo[curr] = a
        if not a:
                return False, []
        p = p1 if a1 else p2
        return True, p + [curr]


if __name__ == "__main__":
    r = 2
    c = 3
    mines = [(0,1),]
    print(find_path_main(mines,r,c))