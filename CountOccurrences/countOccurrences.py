
'''
Author Todian Mishtaku
'''

# Parameters:
#  arr: List[int]
#  num: int
# return type: int

def countOccurrences(arr, num):
    if(0==len(arr)):
        return 0
    elif (arr[0]==num):
        return 1+countOccurrences(arr[1:], num)
    else:
        return countOccurrences(arr[1:], num)
    

arr=[2,3,4,4,5,8,5,5,9,8]  
num=3  
print(countOccurrences(arr, num))