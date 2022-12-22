# Parameters:
#  matrix: List[List[int]]
# return type: int

'''
Author:Todian Mishtaku

Complexity:

Time O(2^(nxm)) because for each cell we try two directions:
2 x 2 x 2 x ... x 2    (nxm times 2 multiplied by 2

Space O(n+m) because stack size is constantly proportional 
to length of the path which is n+m-1 cells

Each element(record) of the recursive stack 
has maximally memory size equal to some constant C

O(c x (n+m)) =O(n+m)  

'''

def minimumCostPath(matrix,row=0,col=0):
    if(row==len(matrix) or col==len(matrix[0])):
        return float('inf')
    
    elif ((row==(len(matrix)-1)) and ((col==(len(matrix[0])-1)))): 
        return matrix[row][col]
    
    else: 
        opt1= matrix[row][col] + minimumCostPath(matrix,row+1,col)
        opt2= matrix[row][col] + minimumCostPath(matrix,row,col+1)
        return min(opt1,opt2)
        

matrix1=[[3,12,4,7,10],[6,8,15,11,4],[19,5,14,32,21],[1,20,2,9,7]]# result =54
matrix2=[[3,1,7,5],[6,8,4,2]]# result =17
matrix3=[
         [3,12,4,7,10,8,15,11,4,6],
         [19,5,14,32,21,1,20,2,9,7],
         [3,12,4,7,10,8,15,11,4,3],
         [19,5,14,32,21,1,20,2,9,7]] # result =90
print(minimumCostPath(matrix3)) 

