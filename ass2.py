import numpy as np 
# a=np.array([1,2,3,4,5,6,7,8,9,10])
# na=a.reshape(2,5)
# print(na)

# arr=np.array([[1,2,3],[2,3,6],[6,7,8]])
# even=arr[arr%2==0]
# print('Even numbers:',even)
# third_col=arr[:,2]
# print("elements of third column:",third_col)


# b=np.array([[2,2,3],[4,5,2],[7,3,9]])
# sq_mat=np.linalg.det(b)
# print(sq_mat)

# i=np.array([[1,4],[3,4]])
# inv=np.linalg.inv(i)
# print(inv)

# A = np.array([[2, 3],[4, -1]])
# b = np.array([10, 5])
# x = np.linalg.solve(A, b)
# print(x)

# matrix=np.array([[2,4,6],[1,3,5],[0,0,0]])
# is_singular=np.linalg.det(matrix)==0
# det=np.linalg.det(matrix)
# print(det)

# a1=np.array([2,3,5])
# a2=np.array([1,4,6])
# result=np.dot(a1,a2)
# print(result)

# a3=np.array([2,3,5])
# a4=np.array([1,4,6])
# result=np.inner(a3,a4)
# print(result)

# mat=np.array([[1,2],[3,4]])
# res_mat=2.5*mat
# result=np.round(res_mat).astype(int)
# print(result)


arr1 = np.array([[1,2,3]])
arr2 = np.array([[4,5,6]])
arr = np.concatenate((arr1, arr2), axis=0)
print(arr)






