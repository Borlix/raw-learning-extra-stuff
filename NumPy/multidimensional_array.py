import numpy as np

array1 = np.array('')
# print(array1.ndim) = returns 0 diminsional

array2 = np.array(['a','b','c'])
# print(array2.ndim) = returns 1 diminsional
array3 = np.array([['a','b','c'],
                    ['d','e','f']])
# print(array3.ndim) = returns 2 diminsional
array = np.array([[['a','b','c'],
                    ['d','e','f'],
                    ['g','h','i']]])
print(array.ndim) 
print(array.shape)
print(array.size)
print(array [0] [1] [2])