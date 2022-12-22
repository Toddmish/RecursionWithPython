'''
Author: Todian Mishtaku
Solution with Dynamic programming (not with recursion)

matrix with n rows and m columns

Complexity:

Time: O(nxm)
(Additional) Space: O(nxm)

'''

def minimumCostPath(matrix):
    rows= len(matrix)
    cols=len(matrix[0])
    
    costs=[ [0 for i in range(cols)] for j in range(rows) ]
    #costs=[  [0] * cols  for j in range(rows) ]
    #costs=[[0]*cols] *rows <- ATTENTION see the effect when costs[0][0]=2
    #costs[0][0]=2
    #print(costs)
    
    costs[0][0]=matrix[0][0]
    
    for c in range(1,cols):
        costs[0][c]=costs[0][c-1]+matrix[0][c]
        
    for r in range(1,rows):
        costs[r][0]=costs[r-1][0]+matrix[r][0]
    
    for row in range(1,rows):
        for col in range(1,cols):
            costs[row][col]=matrix[row][col] + min(costs[row-1][col],costs[row][col-1])
           
    return costs[rows-1][cols-1]    
     

matrix1=[[3,12,4,7,10],[6,8,15,11,4],[19,5,14,32,21],[1,20,2,9,7]]# result =54
matrix2=[[3,1,7,5],[6,8,4,2]]# result =17
matrix3=[
         [3,12,4,7,10,8,15,11,4,6],
         [19,5,14,32,21,1,20,2,9,7],
         [3,12,4,7,10,8,15,11,4,3],
         [19,5,14,32,21,1,20,2,9,7]] # result =90
print(minimumCostPath(matrix3)) 
    