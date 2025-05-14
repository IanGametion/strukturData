#Review
#List
#comma-separated values
#square brackets []
#no need same data type

lst1 = ['cs', 'si', 2002, 2004]
lst2 = [1, 3, 5, 7]
lst3 = ["a", "e", "i", "o", "u"]

print ("lst1[0]: ", lst1[0])
print ("lst2[1:3]: ",lst2[1:3])
print ("lst3[1:]: ", lst3[1:])
print ("lst3[:3]: ", lst3[:3])
print ("lst3[:]: ", lst3[:])

lst3[2] = "b"
print ("lst3[:]: ", lst3[:])

del lst3[2]
print ("lst3[:]: ", lst3[:])
del lst3[2:]
print ("lst3[:]: ", lst3[:])

lst3.insert(2,"o")
print ("lst3[:]: ", lst3[:])
