
def getSubstrings(s,i=0,output=[]):
    # your code here
    if(i==len(s)):
        return output
    else:
        for j in range(i+1,len(s)+1):
            print(str(i)+ " "+str(j-1))
            #print(s[i:j])
            output.append(s[i:j])
        getSubstrings(s,i+1,output)
        return output
        
        

print(getSubstrings("ABC"))   


