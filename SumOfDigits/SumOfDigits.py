# Parameters:
#  n: int
# return type: int

'''

Time: O(logn)
Space: O(logn) roughly we create 3 x logn variables when we sum up in each call

'''

def sumOfDigits(n):
    if (0==n):
        return 0 # T(0)=1
    return (n%10)+sumOfDigits(n//10) # 1+ T(n/10) 


print(sumOfDigits(2345))

'''

T(0)=1

T(n)= T(n/10) =T(n/10) + O(1)

This is of type:


T(n)= aT(n/b) + f(n)  ;hence,

T(n)= 1T(n/10) + O(1) ;hence,

a=1 b=10  log10(1) =0

c=? f(n)=O(1)=O(n^c)=> c=0

because logb(a)==c from Master Recurrence Theorem => T(n)=O(n^c x logn ) <=>
<=>T(n)=O(n^0 x logn)= O(logn) 

OR 

Recursion method is called as many time as it is the number of digits i.e,
 
log10(n)  briefly O(n)=logn

MASTER THEOREM

Case 1: c < log(a) [base b] => Time Complexity = O(n ^ log(a) [base b])
Case 2: c = log(a) [base b] => Time Complexity = O((n ^ c) * log(n) )
Case 3: c > log(a) [base b] => Time Complexity = O((n ^ c))

 
'''