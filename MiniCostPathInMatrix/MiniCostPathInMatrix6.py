'''
Author: Todian Mishtaku 
This version contains only one recursive case (two recursive calls).

'''
def minimumCostPath(matrix,row=0,col=0,cost=0):
    
    if(row==len(matrix) or col==len(matrix[0])):
        return float('inf')
    
    elif row==len(matrix)-1 and col==len(matrix[0])-1: 
        return cost+matrix[row][col] 
    
    elif row==len(matrix)-1: 
            return cost+sum(matrix[row][col:])
        
    elif col==len(matrix[0])-1:
            listOfRemainedRows=matrix[row:]
            remainedElementsOfLastCol=[remainedRow[col:][0] for remainedRow in listOfRemainedRows]
            return cost+ sum(remainedElementsOfLastCol)
    
    
    else:
        return min(minimumCostPath(matrix,row+1,col,cost+matrix[row][col]),
                                     minimumCostPath(matrix,row,col+1,cost+matrix[row][col]))
    


matrix1=[[3,12,4,7,10],[6,8,15,11,4],[19,5,14,32,21],[1,20,2,9,7]]# result =54
matrix2=[[3,1,7,5],[6,8,4,2]]# result =17
matrix3=[
         [3,12,4,7,10,8,15,11,4,6],
         [19,5,14,32,21,1,20,2,9,7],
         [3,12,4,7,10,8,15,11,4,3],
         [19,5,14,32,21,1,20,2,9,7]] # result =90
print(minimumCostPath(matrix3)) 

'''
A = [[1,2,3,1,5],[1,2,3,4,6],[1,2,3,8,7]]

list=[sublist[3:] for sublist in A]
print(list)

list=[sublist[4:] for sublist in A]
print(list)

ints = [item[0] for item in list]
print(ints)
 #or
list=[sublist[4:][0] for sublist in A]
print(list)
'''



