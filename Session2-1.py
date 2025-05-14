arr_one = [11,12,5,2] # array one dimension
# for x in arr_one:
#     print(x)

arr_two = [[11,12,5,2],
           [15,6,10,5],
           [10,8,12,5]] # array two dimension
# for x in arr_two:
#     for y in x:
#         print(y)

arr_two.insert(2, [8,6,10,3]) # insert ke data 2 
print(arr_two)

arr_two[0][3] = 8 # update data baris ke 1, ke kolom ke 4
print(arr_two)

del arr_two[2] # hapus data ke 2
print(arr_two)