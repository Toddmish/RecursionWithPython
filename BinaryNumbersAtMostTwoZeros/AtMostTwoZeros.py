def binaryNumbers(n):
    str=['1'] * n
    strings=[]
    #print(str)
    
    def rec(str,i=0, zeroCount=0):
        if(i==len(str)):
            strings.append(''.join(str))
            return
        if(zeroCount<2):
            str[i]='0'
            rec(str,i+1,zeroCount+1)
            str[i]='1'
            rec(str,i+1,zeroCount)
            
        else:
            rec(str,i+1,zeroCount)
        
     
    
    rec(str,0,0)
    return strings
    #print(strings)
    
print(len(binaryNumbers(4)))
    
