# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")

# Parameters:
#  s: str
# return type: str

        
def reverse(s):
    #return doReverse(s, len(s)-1)
    #return doReverse3(s)
    
    rev=[]
    doReverse22(s,rev,0) 
    return ''.join(rev)
    
    
'''
Time O(n2)
Memory:O(n)  
'''
def doReverse(s, i):
    if(i<0):
        return "" 
    else:
        return s[i] + doReverse(s,i-1)

'''
Time O(n2)
Memory:O(n)  
'''
def doReverse2(s, rev,i):
    if(i==len(s)):
        return "" 
    else:
        doReverse2(s,rev,i+1)
        rev+=s[i]
    
def doReverse4(str,rev="",i=0):
    if(i==len(str)):
        return rev
    else:
        return doReverse4(str,str[i]+rev,i+1)
        
'''
Time O(nlogn)
Memory:O(n)  <=2n-1
'''
def doReverse3(s):
    if(len(s)<=1):#<----  pay attention to condition ,what if '='' gets removed
        return s[0] 
    else:
        mid=len(s)//2
        left=s[:mid]
        right=s[mid:]
        return doReverse3(right) + doReverse3(left)
    

    
    '''
Time O(n)
Memory:O(n)  
'''
def doReverse22(s, rev,i):
    if(i==len(s)):
        return  
    else:
        doReverse22(s,rev,i+1)
        rev.append(s[i])  
    


ss="123456789"   
print(reverse(ss))

print(doReverse4(ss))
print(doReverse3(ss))