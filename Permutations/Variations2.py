# Parameters:
#  arr: List[int]
# return type: List[List[int]]



def getPermutations(arr):  

    allPerm=[]
    
    def generate(arr,n,phrase=[]):  
   
        if len(phrase)==n:
                allPerm.append(phrase.copy())
            
        else:       
            
            for d in arr:
                
                newArr=arr.copy()
                newArr.remove(d)
                
                phrase.append(d)
                generate(newArr,n,phrase)
                phrase.remove(d)

    
        return allPerm
     
    return generate(arr,len(arr))
    
 
arr1=[1,2,3]   
arr2=[1,2,2] 
arr3=[2,2]   
arr4=[1,2] 
arr5=[1,2,2]

print(getPermutations(arr5))
    
    
    
    
    