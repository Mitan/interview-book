def find_path_main(mines, r, c):
    if r == 0 or c == 0:
        raise Exception("wrong dimensions")
    failed_points = []
    path = []
    ans = find_path(mines, (r - 1, c - 1), failed_points, path)
    if ans:
        return path
    return None


def find_path(mines, curr, failed_points, path):
        c1, c2 = curr
        if curr in mines or curr in failed_points or c1 < 0 or c2<0:
            return False

        if curr == (0,0) or \
                find_path(mines, (c1 - 1, c2), failed_points, path) or\
                find_path(mines, (c1, c2-1), failed_points, path):
            path.append(curr)
            return True

        failed_points.append(curr)
        return False


if __name__ == "__main__":
    r = 2
    c = 3
    mines = [(0,1), (0,2)]
    print(find_path_main(mines,r,c))