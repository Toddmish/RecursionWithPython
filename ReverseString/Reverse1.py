# Parameters:
#  s: str
# return type: str

        
def reverse(s):
    return doReverse(s, len(s)-1)

'''
Time O(n2)
Memory:O(n)  
'''
def doReverse(s, n):
    if(n<0): return "" 
    return s[n] + doReverse(s,n-1)
    
s1="123456789" 
s2="abc" 
s3="" 
s4="abbad"
print(reverse(s4))

'''
T(0)=1
T(n)=n+T(n-1)=T(n-1)+n    =>T(n-1)=T(n-2)+n-1 =>
T(n)=[T(n-2)+n-1] +  n
T(n)={[T(n-3)+n-2]+n-1} + n= T(n-3)+ n-2 + n-1 +n
 .
.
.
T(n-k)=T(n-k)+  (n-k+1)+ (n-k+2)+...+ n

T(n)= T(n-n)+ 1+2+3+..+n =1 + nx(n+1)/2 =O(n^2)

''' 