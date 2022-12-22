#Non-recursive version using the smallest greatest number

'''
Input:     [2,3,8,5,1]
           [2,5,8,3,1]
Output:    [2,5,1,3,8]  -> This is the next (smallest) greatest number

Input:     [2,5,1,3,8]
           [2,5,1,8,3]
Output:    [2,5,1,8,3]
            

'''
#input arr is sorted in ascending order
def getNextPermutation(arr):
    
    print("getNextPermutation: Input array: "+ str(arr))
    i=len(arr)-2
    
    while i>=0 and arr[i]>=arr[i+1]: i-=1
        
    #already sorted in descending order    
    if -1==i: return arr
    
    #else the arr[i] holds the first element from the right 
    #that broke the ascending order
    
    #Let's find the first element to the right of arr[i] 
    #that is greater than_arr[i]
    
    j=len(arr)-1
    
    while arr[j]<=arr[i]: j-=1
        
    (arr[i],arr[j])=(arr[j],arr[i])
       
    arr[i+1:]=arr[:i:-1]
    
    return arr    
    



def getPermutations(arr):  
    
    print("Input array: "+ str(arr))
    
    if len(arr)<2:
        return [arr]

    minPerm=sorted(arr)
    maxPerm=sorted(arr,reverse=True)
    
    allPermutations=[]    
    allPermutations.append(minPerm)

    
    while arr!= maxPerm:
        arr=getNextPermutation(arr)
        allPermutations.append(arr.copy())
    
    
     
    return allPermutations


print( getNextPermutation([2,5,1,3,8]) )

arr1=[1,2,3]   
arr2=[1,2,2] 
arr3=[2,2]   
arr4=[1,2] 
arr5=[1,2,2]

print(getPermutations(arr2))