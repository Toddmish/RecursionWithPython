# Parameters:
#  s: str
# return type: str


def reverse(s):
    return doReverse(s)
        
'''
Time O(nlogn)
Memory:O(n)  <=2n-1
'''
def doReverse(s):
    if(len(s)<=1):#<----  pay attention to condition ,what if '='' gets removed
        return s[0] 
    else:
        mid=len(s)//2
        left=s[:mid]
        right=s[mid:]
        return doReverse(right) + doReverse(left)
    
        
        
s1="123456789" 
s2="abc" 
s3="" 
s4="abbad"
print(reverse(s1))