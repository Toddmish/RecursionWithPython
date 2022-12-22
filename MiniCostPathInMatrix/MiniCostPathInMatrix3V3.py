'''
Author: Todian Mishtaku

Here is measured the effect of memoization


Time Complexity with memo is roughly 2xnxm; hence, O(nxm) 
 
'''

def minimumCostPath(matrix):
    rows= len(matrix)
    cols= len(matrix[0])
    memo= [ [ -1 for i in range(cols) ] for j in range(rows)]
    
    
    def mcp(n,matrix,row=0,col=0):
    
        n[0]+=1
        
        if row==len(matrix) or col==len(matrix[0]):
            return float('inf')
        
        elif row==len(matrix)-1 and col==len(matrix[0])-1: 
            return matrix[row][col]
        
        #Try removing this case and see how n[0] increases
        elif memo[row][col]!=-1:
            return memo[row][col]
        
        elif row==len(matrix)-1:
                return matrix[row][col]+mcp(n,matrix,row,col+1)
        elif col==len(matrix[0])-1:
                return matrix[row][col]+mcp(n,matrix,row+1,col)
            
        else:
            memo[row][col]=matrix[row][col]+ min(mcp(n,matrix,row+1,col),mcp(n,matrix,row,col+1))
            return memo[row][col]
    
    n=[0] # just a counter to measure how many times recursive function is called
    res= mcp(n,matrix)
    print(n[0])
    return res


matrix1=[[3,12,4,7,10],[6,8,15,11,4],[19,5,14,32,21],[1,20,2,9,7]]# result =54
matrix2=[[3,1,7,5],[6,8,4,2]]# result =17
matrix3=[
         [3,12,4,7,10,8,15,11,4,6],
         [19,5,14,32,21,1,20,2,9,7],
         [3,12,4,7,10,8,15,11,4,3],
         [19,5,14,32,21,1,20,2,9,7]] # result =90
print(minimumCostPath(matrix3)) 