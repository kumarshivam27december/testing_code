# Program to transpose a matrix using a nested loop

X = [[12,7,5,1],
    [4,5,4,1],
    [3,8,2,5]]

result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],[0,0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)