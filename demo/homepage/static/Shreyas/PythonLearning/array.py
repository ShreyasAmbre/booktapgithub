from array import *
# i means integer & d means float to metion the datatype of the value when using array
a = array('i', [1, 2, 3, 4])
d = array('i', [10, 20, 30, 40])
b = array('d', [1.1, 2.4, 3.3, 4.2])
print(a, b)

# ************** Array Concatenation******************
# NOTE :-  Concatination will only work when TWO DIFFERENT ARRAYS HAVING SAME DATATYPES
c = array('i')
res1 = a + d
print(res1)

# ********** Slicing of Array ***************
# [from which index no. to start fecting values : Till which index no. should stop fetching value]
print(a[0:5])


