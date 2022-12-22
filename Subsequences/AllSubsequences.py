def getSubsequences(s,i=0,output=[]):
    # your code here
    
    if(i==len(s)-1):
        return [s[i],'']
    else:
        
        substrings=getSubsequences(s,i+1,output)
        output=[]
        for w in substrings:
            newWord=s[i]+w
            output.append(newWord)
        return output+substrings
    
print(getSubsequences('abc'))    

