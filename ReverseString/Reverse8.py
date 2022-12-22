'''
Time O(n)
Memory:O(1)  
'''
def reverse(str):
    left=0
    right=len(str)-1
    
    while(left<right):
        str[left],str[right]=str[right],str[left]
        left +=1
        right-=1
    return ''.join(str)
    
    
    
s1="123456789" 
s2="abc" 
s3="" 
s4="abbad"
print(reverse(list(s2))) # Memory: O(n) because we create list   