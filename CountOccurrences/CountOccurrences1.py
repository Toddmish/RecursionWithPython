# Parameters:
#  arr: List[int]
#  num: int
# return type: int

'''
Time: O(n)
Additional memory: O(n) stack maximally reaches length n+1 at base case 
                        (then multiplied by a const)
'''

def countOccurrences(arr, num,i=0):
    if(i==len(arr)):
        return 0
    elif (arr[i]==num):
        return 1+countOccurrences(arr, num,i+1)
    else:
        return countOccurrences(arr, num,i+1)
    

arr=[2,3,4,4,5,8,5,5,9,8]  
num=5
print(countOccurrences(arr, num))

'''
T(0)=1
T(n)=1+T(n-1)=T(n-1)+1    =>T(n-1)=T(n-2)+1 =>
T(n)=[T(n-2)+1] +  1 =T(n-2)+2
T(n)=...=T(n-3)+3
 .
.
.
T(n-k)=T(n-k)+  k

T(n)= T(n-n)+ n =1 + n =O(n)

''' 