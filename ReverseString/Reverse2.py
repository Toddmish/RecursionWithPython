# Parameters:
#  s: str
# return type: str

        
def reverse(s):
    return ''.join(doReverse(s))


'''
Time O(n2)
Memory:O(n)  
'''
def doReverse(s, rev=[], i=0):
    if(i==len(s)):
        return "" 
    else:
        doReverse(s,rev,i+1)
        rev+=s[i]
        return rev
    
        
        
s1="123456789" 
s2="abc" 
s3="" 
s4="abbad"
print(reverse(s4))