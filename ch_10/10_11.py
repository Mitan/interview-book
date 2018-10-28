def peaks_and_valleys(arr):
    if not arr:
        raise Exception()
    l = len(arr)
    for i in range(l - 1):
        if (i % 2 == 0 and arr[i] > arr[i + 1]) or (i % 2 == 1 and arr[i] < arr[i + 1]):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


if __name__ == "__main__":
    a = [4,5,6,2,4,4,5,6,10]
    print(peaks_and_valleys(a))
