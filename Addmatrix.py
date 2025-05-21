import array as arr

def create_Mtx2D(row, col):
    i = 0
    j = 0
    mtx = []
    for i in range(row):
        rw = []
        for j in range(col):
            m = i + 1
            n = j + 1
            element = int(input("Enter [" + str(m) + "][" + str(n) + "]: "))
            rw.append(element)
        mtx.append(rw)
    return mtx

def print_Mtx2D(mtx):
    for row in mtx:
        print(row)

def add_Mtx2D(mtx1, mtx2):
    rw, cl = len(mtx1), len(mtx1[0])
    mtx = [[0]* cl] * rw
    mtx = [[mtx1[i][j] + mtx2[i][j] for j in range(cl)] for i in range(rw)]
    return mtx

row = int(input("Enter number of rows: "))
col = int(input("Enter number of columns: "))
print("Enter first matrix: ")
mtx1 = create_Mtx2D(row, col)
print("Enter second matrix: ")
mtx2 = create_Mtx2D(row, col)
print("First matrix: ")
print_Mtx2D(mtx1)
print("Second matrix: ")
print_Mtx2D(mtx2)
mtx = add_Mtx2D(mtx1, mtx2)
print("Results:")
print_Mtx2D(mtx)
