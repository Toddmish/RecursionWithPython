'''
Author Todian Mishtaku
Time: O(n)
Additional memory: O(1) 
'''


'''
Iterative
'''

def hasAdjacentDuplicates(s,i=0):
    for i in range(0,len(s)-1):
         if s[i]==s[i+1]:
             return True
    return False
    

s1="abcdadb"    
s2="bc"   
s3="bb"
s4="ananaa"
print(hasAdjacentDuplicates(s1))