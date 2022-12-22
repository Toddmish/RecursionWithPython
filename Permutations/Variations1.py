# Parameters:
#  arr: List[int]
# return type: List[List[int]]



def getPermutations(arr):  

    
    allPerm=[]
    
    def generate(arr,phrase=[]):  
   
        if len(phrase)==len(arr):
            perm=[]
            for idx in phrase:
                perm.append(arr[idx])
            allPerm.append(perm)
            
        else:       
            
            for idx in range(0,len(arr)):
                if not idx in phrase:
                    phrase.append(idx)
                    generate(arr,phrase)
                    phrase.remove(idx)
    
        return allPerm
     
    return generate(arr)
    
 
arr1=[1,2,3]   
arr2=[1,2,2] 
arr3=[2,2] 
  

print(getPermutations(arr1))
    
    
    
    
    