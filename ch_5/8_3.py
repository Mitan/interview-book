def find_magic_main(arr):
    return find_magic(arr, 0, len(arr) - 1, 0, len(arr) - 1)


def find_magic(arr, left, right, min_global, max_global):
    if left > right or left < min_global or right > max_global:
        return False
    middle = (left + right) // 2
    gap = arr[middle] - middle
    if gap == 0:
        return True
    elif gap > 0:
        return find_magic(arr, left, middle - 1, min_global, max_global) or\
               find_magic(arr, middle + gap, right, min_global, max_global)
    else:
        return find_magic(arr, middle + 1, right, min_global, max_global) or\
               find_magic(arr, left, middle - gap, min_global, max_global)


if __name__ == "__main__":
        arr = [4,4,4,4,5, 6,6,6,9]
        print(find_magic_main(arr))
