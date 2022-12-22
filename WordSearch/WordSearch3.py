# Parameters:
#  board: List[List[char]]
#  word: str
# return type: bool
from pickle import TRUE

'''
Author: Todian Mishtaku

'''

def okToGo(board,word,pos,marked,i,j):
    
    
    if i<0 or i>= len(board) or j<0 or j>=len(board[0]):
        #print(" (exceed,i,j)= ("" " + str(i)+" "+str(j)+")" )    
        return False
    
    if 1==marked[i][j]:
        #print(" (It is marked,i,j)= ("" " + str(i)+" "+str(j)+")" )  
        return False
    
    if word[pos]!=board[i][j]:
        return False
    
    return True
    

def go(board, word,pos,marked,i=0,j=0,count=0):
 
    if pos==len(word):
        return True
    
    if not okToGo(board, word,pos, marked, i, j):      
        return False
    
    #print(board[i][j])
    marked[i][j]=1
    #print(" (marking,i,j)= ("" " + str(i)+" "+str(j)+")" )

    if go(board, word,pos+1,marked,i,j+1,count): return True
    if go(board, word,pos+1,marked,i,j-1,count): return True
    if go(board, word,pos+1,marked,i+1,j,count): return True
    if go(board, word,pos+1,marked,i-1,j,count): return True

    '''
    If none of the above directions gives solution,
    release the cell to be considered for other paths
    '''
    marked[i][j]=0
                      
    return False


def exist(board, word):
    marked=[[0]* len(board[0]) for i in range(0,len(board)) ]
    for i in range(0,len(board)):
        for j in range(0,len(board[0])):
            if board[i][j]==word[0]:
                if go(board, word,0,marked,i,j):
                    return True
    return False       


def run():
    
    board=[['K','I','N','T'],
           ['B','I','N','S'],
           ['G','N','Y','I'],
           ['U','O','E','D'],
           ['D','I','B','V']]
    
    #board=[['A','b','C','I','N','S', 'I','D','E']]
    #Too wrong -> marked=[[0]*len(board[0])]* len(board)
    marked=[[0]* len(board[0]) for i in range(0,len(board)) ]
    
    print(board)
    print(marked)
    word='INSIDE'
    return exist(board, word)
        
print(run())





