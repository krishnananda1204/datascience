import numpy as np
X=np.array([[1,2,3],[4,5,6],[7,4,1]])
Y=np.array([[5,7,6],[2,1,8],[4,3,9]])

print("7X+Y^3 =\n",(Y**3)+(7*X))
print("\n")
print("Matrix mutiplication of X & Y:")
print (np.matmul(X,Y))
print("\n")
print("Diagonal of X:")
print(np.diag(X))
print("Diagonal of Y:")
print(np.diag(Y))
print("\n")
print("Rank of matrix X:")
print(np.linalg.matrix_rank(X))
print("Rank of matrix Y:")
print(np.linalg.matrix_rank(Y))

