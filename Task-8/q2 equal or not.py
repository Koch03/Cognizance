import numpy as np
a = np.random.randint(0,3,5)
print(a)
b = np.random.randint(0,3,5)
print(b)
array_equal = np.allclose(a,b)
print(array_equal)