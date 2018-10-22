from bisect import bisect_left


def find_index(arr, val):
    if not arr:
        return -1
    l = len(arr)
    if arr[0] == val or arr[-1] == val:
        return 0 if arr[0] == val else l - 1


    if arr[0] < arr[-1]:
        return bisect_left(arr, val)

    max_index = find_max(arr, 0, l - 1)

    if arr[0] > val:
        return bisect_left(arr, val, lo=max_index + 1)
    else:
        return bisect_left(arr, val, hi=max_index)


def find_max(arr, low, high):
    if low > high:
        return -1
    middle = (low + high) // 2
    if arr[middle] > arr[middle + 1]:
        return middle
    if arr[middle] > arr[low]:
        return find_max(arr, middle + 1, high)
    else:
        return find_max(arr, low, middle - 1)


if __name__ == "__main__":
        arr = [4,5,6,7, 1, 2, 3]
        print(find_index(arr, 7))
