# Parameters:
#  arr: List[int]
# return type: List[List[int]]


def getPermutations(arr):  

    
    def generate(arr):  
   
        if len(arr)<2:
                return [arr]
        output=[]
        for d in arr:             
            newArr=arr.copy()
            newArr.remove(d)             
            perm=generate(newArr)
            for pr in perm:
                output.append(pr+[d])       
        return output
     
    return generate(arr)
    
 
arr1=[1,2,3]   
arr2=[1,2,2] 
arr3=[2,2]   
arr4=[1,2] 
arr5=[1,2,2]
print(arr1[:2])

print(getPermutations(arr3))
    
    
    
    
    