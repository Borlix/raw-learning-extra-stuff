import numpy as np
X = np.array([
        [2,1],
        [4,3],
        [6,5]])
w = np.array([3,2])
b = 1

y = X @ w+b
print(y)