def getSubsequences(s):
    
    finaloutput=[]
    
    def doGetSubsequences(s,i=0):
        if(i==len(s)-1):
            finaloutput.extend([s[i],''])
        else:
            doGetSubsequences(s,i+1)
            output=[]
            for w in finaloutput:
                newWord=s[i]+w
                output.append(newWord)
            finaloutput.extend(output )
  
    doGetSubsequences(s,0)
    return finaloutput
   
print(getSubsequences('abc'))