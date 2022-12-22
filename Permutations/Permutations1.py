# Parameters:
#  arr: List[int]
# return type: List[List[int]]



def getPermutations(arr):  
    allPerm=[]
    l=len(arr)
    def generate(arr,l,phrase=[]):  
 
        if len(phrase)==l:
            allPerm.append(phrase.copy())        
        else: 
   
            for idx in range(0,len(arr)):
                #If the element was previously considered within 
                #this 'for' loop we skip it. This is to avoid duplications
                if not (arr[idx] in arr[:idx]):
                    d=arr[idx]
                    newArr=arr.copy()
                    newArr.remove(d)                 
                    
                    phrase.append(d)
                    generate(newArr,l,phrase)
                    phrase.remove(d)
    
        return allPerm
    
    return generate(arr,len(arr))
    
 
arr1=[1,2,3]   
arr2=[1,2,2] 
arr3=[2,2]   


print(getPermutations(arr3 ))
    
    
    
    
    