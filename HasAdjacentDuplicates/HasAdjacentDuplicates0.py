# Parameters:
#  s: str
# return type: bool

'''
Author: Todian Mishtaku

Time: O(n^2)
Additional memory: O(n?)
'''

'''
Tail recursive
'''
def hasAdjacentDuplicates(s):
    if(len(s)<2):
        '''
        It means we traversed over the whole string and did not find any adjacent duplication; hence,
        it returns False which will be propagated up to the very first call without changing in True.
        '''
        return False # T(0) =O(1)
    elif(s[0]==s[1]):
        '''
            If an adjacent duplication is found the recursion does not go deeper; it just propagates the 'True' value up to the very first call 
        '''
        return True # T(0) =O(1)
    else: 
        return hasAdjacentDuplicates(s[1:]) # slicing costs O(n-1) while the call T(n-1)
    
    
    
s1="abcdadb"    
s2="abcddadb"   
print(hasAdjacentDuplicates(s2))

'''
Time complexity analysis:

T(0)=1
T(n)= T(n-1)+n-1 (I) => T(n-1)= T(n-2)+ n-2, T(n-2)= T(n-3)+ n-3,  ....
T(n)=  T(n-2)+n-2 +n-1 =T(n-2)+2n-2
T(n)=T(n-k)+kn-k
.
.
.
T(n)=1 + nxn-n= 1+ nx(n-1) =nx(n-1)= O(n^2)
 

'''