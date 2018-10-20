def sort_boxes(boxes):
    l = len(boxes)
    if l == 0:
        return 0
    boxes = sorted(boxes, key = lambda x: x[0])
    results = [0 for _ in range(l)]
    results[0] = boxes[0][0]
    for i in range(1, l):
        current_max = 0
        w, d = boxes[i][1:]
        for k in range(i):
            if boxes[k][1] < w and boxes[k][2] <  d and results[k] > current_max:
                current_max = results[k]
        results[i] = current_max + boxes[i][0]

    return max(results)


if __name__ == "__main__":
    boxes = [(8,0,0),(10,3,2), (5,3,9), (2,2,8), (9,1,1)]
    print(sort_boxes(boxes))
