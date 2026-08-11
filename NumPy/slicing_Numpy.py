import numpy as np

array = np.array  ([[1,2,3,4],
                    [5,6,7,8],
                    [9,10,11,12]])
# array[start:stop:step]

print(array[0])     # returns row at indx 0
print(array[1:3])   # returns row from 1-3
print(array[0:3:2]) # returns row from 0-2
print(array[::1])   # returns full array
print(array[::-1])  # returns revers array
print(array[:,0])   # returns colum at indx 0
print(array[:,1])   # returns colum at indx 1
