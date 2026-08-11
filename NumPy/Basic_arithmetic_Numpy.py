# Scaler Arithmetic 

import numpy as np
num = np.array([1,2,3])
print( num + 1)
print( num - 1)
print( num * 2)
print( num / 2)
print( num % 2)
print( num ** 2)

# Vectorized Arithmetic

print(np.sqrt(num))
print(np.ceil(num)) # Return same cause 'num' do not have decimal values
print(np.floor(num))# Return same cause 'num' do not have decimal values
#There are many more, Things will get done slowy each take by take !

# practice :
radii = np.array([3,4,5])
print(np.pi *radii**2)