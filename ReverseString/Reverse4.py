'''
Time O(n^2)
Memory:O(n)  
'''

def reverse(str,rev="",i=0):
    if(i==len(str)):
        return rev # T(0) =O(1)
    else:
        return reverse(str,str[i]+rev,i+1) #T(n-1) + n . 
                  #because concatenation time complexity is n 
    

s1="123456789"
s2="abc" 
s3="" 
s4="abbad"

print(reverse(s1))

'''
T(0)=1
T(n)= T(n-1)+n (I)     From (I) => T(n-1)=T(n-2)+n-1 =>
T(n)= [T(n-2)+n-1] + n From (I) => T(n-2)=T(n-3)+n-2 =>
T(n)=  T(n-3)+n-2 + n-1 + n
T(n) = T(n-k) + n-k+ n-k+1 +n

T(n)=T(n-n) + 1+2+...+n =1 + nx(n+1)/2 = O(n^2) 

'''