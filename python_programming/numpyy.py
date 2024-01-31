# import numpy as np

# arr = np.array([1, 2, 3, 4])

# print(arr.dtype)

# import numpy as np

# arr = np.array(['apple', 'banana', 'cherry'])

# print(arr.dtype)


# import numpy as np

# arr = np.array([1, 2, 3, 4], dtype='S')

# print(arr)
# print(arr.dtype)


# import numpy as np

# arr = np.array([1.1, 2.1, 3.1])

# newarr = arr.astype('i')

# print(newarr)
# print(newarr.dtype)

import numpy as np

# arr = np.array([1, 0, 3])

# newarr = arr.astype(bool)

# print(newarr)
# print(newarr.dtype)

# arr = np.array([[[113,456,324],[123,980,456],[435,897,564]]])

# print(arr.shape)



# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# newarr = arr.reshape(4, 3)

# print(newarr)



# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# newarr = arr.reshape(2, 3, 2)

# print(newarr)


# import numpy as np

# arr1 = np.array([[1, 2], [3, 4]])

# arr2 = np.array([[5, 6], [7, 8]])

# arr = np.concatenate((arr1, arr2), axis=0)

# print(arr)



# import numpy as np

# arr = np.array([3, 2, 0, 1])

# print(np.sort(arr))


import numpy as np
arr=np.array([2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,23,89])
newarr=arr.reshape(2,3,3)
print(newarr)

