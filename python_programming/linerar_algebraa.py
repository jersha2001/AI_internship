# import numpy as np

# array1 = np.array([1, 10, 5])
# array2 = np.array([2, 4, 34])

# # use of dot() to perform array multiplication
# result = np.dot(array1, array2)

# print(result)


# import numpy as np

# array1 = np.array([[1, 3], 
#                    [5, 7]])
# array2 = np.array([[2, 4], 
#                    [6, 8]])

# # inner() for 2D arrays
# result = np.inner(array1, array2)

# print(result)


# import numpy as np

# array1 = np.array([1, 3, 5])
# array2 = np.array([2, 4, 6])

# # outer() to perform outer multiplication
# result = np.outer(array1, array2)

# print(result)


# import numpy as np

# # define a square matrix
# array1 = np.array([[1, 3], 
#                   [4, 7]])

# # compute the determinant of array1
# result = np.linalg.det(array1)


# print(result)
 


# import numpy as np

# # define the coefficient matrix A
# A = np.array([[2, 4], 
#              [6, 8]])

# # define the constant vector b
# b = np.array([5, 6])

# # solve the system of linear equations Ax = b
# x = np.linalg.solve(A, b)
# print(x)


# import numpy as np

# # define a 2x2 matrix
# array1 = np.array([[2, 4], 
#                   [6, 8]])

# # compute the inverse of the matrix
# result = np.linalg.inv(array1)

# print(result)


# import numpy as np
# array2=np.array([1,7,3])
# array3=np.array([5,3,9])
# result=np.dot(array2,array3)
# print(result)


# a3=np.array([[1,2],[3,4]])
# a4=np.array([[2, 4], 
#                    [6, 8]])

# result1=np.inner(a3,a4)
# print(result1)

# import numpy as np 
# array = np.array([[1,3],[5,7]])
# result = np.linalg.det(array)
# # print(result)

# result1 = np.linalg.inv(array)

# print(result1)


import numpy as np
p=np.array([3,6,8])
q=np.array([4,7,13])
print(p)
print(q)
print(np.outer(p,q))

