import numpy as np
First = int(input("First Element: "))
Last = int(input("Last Element: "))
arr = np.arange(First, Last+1)
print(arr)
nz = 5
res = np.zeros(len(arr) + (len(arr)-1)*(nz))
res[::nz+1] = arr
print(res)
