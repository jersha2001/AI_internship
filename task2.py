import numpy as np 
# arr=np.array([1,2,3,4,5,6,7,8,9,10])
# newarr=arr.reshape(2,5)
# print(newarr)


# import numpy as np
# arr=np.array([[1,2,3],[2,3,6],[6,7,8]])
# even=arr[arr%2==0]
# print('Even numbers:',even)
# third_col=arr[:,2]
# print("elements of third column:",third_col)



# b=np.array([[2,2,3],[4,5,2],[7,3,9]])
# result=np.linalg.det(b)
# print(result)



# i=np.array([[1,4],[3,4]])
# i=np.linalg.inv(i)
# print(i)


# import numpy as np
# A = np.array([[2, 3],[4, -1]])
# b = np.array([10, 5])
# z = np.linalg.solve(A, b)
# print(z)



# import numpy as np
# matrix=np.array([[2,4,6],[1,3,5],[0,0,0]])
# is_singular=np.linalg.det(matrix)==0
# df=np.linalg.det(matrix)
# print(df)




# a1=np.array([2,3,5])
# a2=np.array([1,4,6])
# result=np.dot(a1,a2)
# print(result)




# mat=np.array([[1,2],[3,4]])
# res_mat=2.5*mat
# df=np.round(res_mat).astype(int)
# print(df)






arr1 = np.array([[1,2,3]])
arr2 = np.array([[4,5,6]])
arr = np.concatenate((arr1, arr2), axis=0)
print(arr)