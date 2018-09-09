def rotate_matrix(mat):
    n = len(mat)
    if n == 0 or len(mat[0]) != n:
       raise Exception("incorrect input")
    for l in range(n // 2):
        for i in range(l, n - 1- l):
            temp = mat[l][i]
            mat[l][i] = mat[n - 1 - i][ l]
            mat[n - 1 - i][ l] = mat[n - 1 - l][ n - 1 - i]
            mat[n - 1 - l][ n - 1 - i] = mat[i][ n - 1 - l]
            mat[i][ n - 1 - l] = temp
    return mat
