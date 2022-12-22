'''
Time: O(n^2)
Additional memory: O(n)
 
'''

def reverse(str):
    if ''==str: return str  # T(0)=1
    return reverse(str[1:]) + str[0] # reverse(str[1:])=T(n-1) and T(+)= n
    
s1="123456789" 
s2="abc" 
s3="" 
s4="abbad"
print(reverse(s1))



'''
Calculations for the time complexity:

T(0)=1
T(n)= T(n-1) + n (concatenation has always the same cost==n)  (I). From (I) T(n-1)=T(n-2) + n ;hence,
T(n)= T(n-2) +n +n= T(n-2) + 2n=T(n-2) + 2n
.
.
.
.
T(n) =T(n-n)+ nxn = 1+n^2 => O(n^2)

'''