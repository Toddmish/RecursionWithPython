# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")


def doPhrases(arr,col1=0,col2=0,col3=0,arrBool=[], output =[] ):
  
    if not ((col1<len(arr[0])) and (col2<len(arr[1])) and (col3<len(arr[2]))):
        return
    
    elif (1==arrBool[col1][col2][col3]):
            return output
    else:
        sentence= arr[0][col1]+ " " + arr[1][col2] + " "  +arr[2][col3]
        output.append(sentence)
        
        arrBool[col1][col2][col3]=1
       
        doPhrases(arr,col1+1,col2,col3,arrBool,output)
        doPhrases(arr,col1,col2+1,col3,arrBool,output)
        doPhrases(arr,col1,col2,col3+1,arrBool,output)
        return output 
    


def phrases(arr):

    col1No=len(arr[0])
    col2No=len(arr[1])
    col3No=len(arr[2])
    arrBool=[[[0 for i in range(0,col3No)] for j in range(0,col2No)] for k in range(0,col1No)]
    print(arrBool)
    return doPhrases(arr,0,0,0,arrBool,[]) 

arr=[['I','You','They'],['love','hate'],['food','games']]
print(phrases(arr))
 
