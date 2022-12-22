# Parameters:
#  arr: List[int]
#  num: int
# return type: int

'''
Time: O(n)
Additional memory: O(1) if the language supports tail recursion optimization, 
                        otherwise O(n) 
'''

'''
Tail-recursive version
'''
def countOccurrences(arr, num,i=0, counter=0):
    if(i==len(arr)):
        return counter #counter will be forward propagated up to the very first caller
    elif (arr[i]==num):
        return countOccurrences(arr, num,i+1,counter+1)
    else:
        return countOccurrences(arr, num,i+1,counter)
    

arr=[2,3,4,4,5,8,5,5,9,8]  
num=5
print(countOccurrences(arr, num))

'''
T(0)=1  (return operation costs O(1)
T(n)=1+T(n-1)=T(n-1)+1 
(+1 here is for the i's increment and 
eventually for the counter's increment)    =>T(n-1)=T(n-2)+1 =>
T(n)=[T(n-2)+1] +  1 =T(n-2)+2
T(n)=...=T(n-3)+3
 .
.
.
T(n-k)=T(n-k)+  k

T(n)= T(n-n)+ n =1 + n =O(n)

''' 