def reverse(str):
    arr=list(str)
    doReverse(arr,0,right=len(arr)-1)
    return ''.join(arr)

def doReverse(str,left,right):
    if left>=right: 
        return
    str[left],str[right]=str[right],str[left]
    doReverse(str,left+1,right-1) 
    


s1="123456789" 
s2="abc" 
s3="" 
s4="abbad"


print(reverse(s1))    