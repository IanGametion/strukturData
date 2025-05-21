import array as arr

def create_Mtx2D(row, col):
    i = 0
    j = 0
    mtx = []
    while i < row:
        rw = []
        while j < col:
            element = int(input("Enter [" + str(i+1) + "][" + str(j+1) + "]: "))
            rw.append(element)
            j = j+1
        mtx.append(rw)
        i = i + 1
    return mtx
            

row = int(input("Enter number of rows: "))
col = int(input("Enter number of columns: "))
print("Enter first matrix: ")
mtx1 = create_Mtx2D(row, col)
