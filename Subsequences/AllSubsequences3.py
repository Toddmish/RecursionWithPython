'''
Previous versions work, but maximal stack depth is reached out earlier
The following one is the best:
 
'''
def getSubsequences(s):
    
    finaloutput=[]
    
    def doGetSubsequences(s,i,subseq):
        if(i==len(s)):
            finaloutput.append(subseq)
        else:
            doGetSubsequences(s,i+1, subseq + s[i])
            doGetSubsequences(s,i+1, subseq)
  
    doGetSubsequences(s,0,"")
    return finaloutput
   
print(getSubsequences('abcgijjpitjypr'))