#Initialize matrix a  
a = [  
        [1, 2, 3],  
        [4, 5, 6],  
        [7, 8, 9]  
    ];  
   
#Calculates number of rows and columns present in given matrix  
rows = len(a);  
cols = len(a[0]);  
   
#Declare array t with reverse dimensions and is initialized with zeroes.  
t = [[0]*rows for i in range(cols)];  
   
#Calculates transpose of given matrix  
for i in range(0, cols):  
    for j in range(0, rows):  
        #Converts the row of original matrix into column of transposed matrix  
        t[i][j] = a[j][i];  
   
print("Transpose of given matrix: ");  
for i in range(0, cols):  
    for j in range(0, rows):  
        print(t[i][j]),  
   
    print(" ");  