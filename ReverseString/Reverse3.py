# Parameters:
#  s: str
# return type: str

'''
Time O(n)
Memory:O(n)  
'''
        
def reverse(s):
    rev=[]
    doReverse(s,rev,0) 
    return ''.join(rev)



'''
Time O(n)
Memory:O(n)  
'''
def doReverse(s, rev,i):
    if(i==len(s)):
        return  
    else:
        doReverse(s,rev,i+1)
        rev.append(s[i]) # or rev+=s[i] 



s1="123456789" 
s2="abc" 
s3="" 
s4="abbad"
print(reverse(s1)) 