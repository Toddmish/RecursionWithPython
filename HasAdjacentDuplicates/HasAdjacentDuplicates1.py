# Parameters:
#  s: str
# return type: bool

'''
Author: Todian Mishtaku

Time: O(n)
Additional memory: O(1) if the language supports tail recursion, otherwise  O(n) stack maximally reaches length n+1 at base case 
                        (then multiplied by a const)
'''

'''
Tail recursive
'''
def hasAdjacentDuplicates(s,i=0):
    if( i+1 > len(s)-1 ):
        '''
        It means we traversed over the whole string and did not find any adjacent duplication; hence,
        it returns False which will be propagated up to the very first call without changing in True.
        '''
        return False  # T(0) =O(1)
    
    elif(s[i]==s[i+1]): 
        '''
            If an adjacent duplication is found the recursion does not go deeper; it just propagates the 'True' value up to the very first call 
        '''
        return True # T(0) =O(1)
    else: 
        return hasAdjacentDuplicates(s,i+1) # i+1 costs O(1) while the call T(n-1)
    
    
    
s1="abcdadb"    
s2="abcddadb"   
print(hasAdjacentDuplicates(s1))


'''
Time complexity analysis:

T(0)=1
T(n)= T(n-1)+1 (I) => T(n-1)= T(n-2)+1, T(n-2)= T(n-3)+1,  ....
T(n)=  T(n-2)+1 +1=T(n-2)+2
T(n)=T(n-k)+1
.
.
.
T(n)=1 + n=O(n)
 

'''