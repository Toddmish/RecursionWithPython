# Parameters:
#  board: List[List[char]]
#  word: str
# return type: bool

def okToGo(board,marked,i,j):
    if i<0 or i>= len(board) or j<0 or j>=len(board[0]):
        return False
    if 1==marked[i][j]:
        return False
    return True
    

def go(board, word,pos,marked,i=0,j=0,ret=False):

    
    if not okToGo(board, marked, i, j):
        return False
    
    if pos==len(word)-1:
        print("found")
        print(marked)
        return True
        
    if board[i][j]==word[pos]:
        marked[i][j]=1
        pos+=1
        ret=True
    else:
        ret=False
        
    right=go(board, word,pos,marked,i,j+1,ret)
    '''
    left=go(board, word,pos,marked,i,j-1,ret)
    up=go(board, word,pos,marked,i+1,j,ret)
    down=go(board, word,pos,marked,i-1,j,ret)       
    '''          
    if board[i][j]==word[pos]:
        marked[i][j]=0
        pos-=1
       
            
    res=right #or left or up or down
            
    return ret and res
        

       
        
        
    
   

def run():
    '''
    board=[['K','I','N','T'],
           ['B','I','N','S'],
           ['G','N','Y','I'],
           ['U','O','E','D'],
           ['D','I','B','V']]
    '''
    board=[['A','b','C','I','N','S', 'I','D','E']]
    marked=[[0]*len(board[0])]* len(board)
    
    print(board)
    print(marked)
    word='INSIDE'
    print(go(board, word,0,marked))
    
run()