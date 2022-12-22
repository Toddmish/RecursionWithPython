'''
Time O(n)
Memory:O(n)  
'''

def reverse(str):
    arr=list(str)  # O(n) time and additional space
    n=len(arr)
    mid=len(arr)//2
    for i in range(mid):# (2 x n/2) swaps 
        arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
    
    return ''.join(arr)

s1="123456789" 
s2="abc" 
s3="" 
s4="abbad"
print(reverse(s1) )


        