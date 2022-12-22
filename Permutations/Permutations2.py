# Parameters:
#  arr: List[int]
# return type: List[List[int]]


def getPermutations(arr):  

    print("Input:" +str(arr))
    def generate(arr):  
   
        if len(arr)<2:
                return [arr]
        output=[]
        for idx in range(len(arr)):
            if arr[idx] not in arr[:idx]:     
                #If the element was previously considered within 
                #this 'for' loop we skip it. This is to avoid duplications        
                newArr=arr.copy()
                newArr.remove(arr[idx])             
                perm=generate(newArr)
                for pr in perm:
                    output.append(pr+[arr[idx]])       
        return output
     
    return generate(arr)
    
 
arr1=[1,2,3]   
arr2=[1,2,2] 
arr3=[2,2]   
arr4=[1,2] 
arr5=[1,2,2]

print(getPermutations(arr2))
    