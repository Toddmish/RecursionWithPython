# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")


    
def phrases(arr):
    
    
    arrBool=[
                [ 
                 [0 for i in range(0,len(arr[2]) )]  
                  
                  for j in range(0,len(arr[1]))
                ] 
          
                for k in range(0,len(arr[0]))
          ]
    
    leng=len(arr)
    
    arrBool1=[0 for i in range(0,len(arr[leng-1]))]
    #arrBool1=[0]*len(arr[leng-1]) <- this is another way
    print(arrBool1)
    
    for i in range(1,-1,-1):
        colNo=len(arr[i])
        arrBool1=[arrBool1 for k in range(0,colNo)] 
    print(arrBool1)
   
    
    
    

    print(arrBool)
        
    
    return doPhrases(arr,0,0,0,arrBool,[]) 
   

def doPhrases(arr,cols,arrBool=[], output =[] ):
    
    leng=len(arr)
    for i in range(0,len(arr)):
        colNo=len(arr[i])
        if(colNo>=cols[i]):
            return 
    
        elif (1==arrBool[col3][col2][col1]):
                return output
        else:
            sentence=""
            for i in range(0,len(arr))
                colNo=len(arr[i])
                sentence= arr[0][colNo]+" "
                output.append(sentence)
            
            arrBool[col1][col2][col3]=1
            for i in range(0,len(arr))
                cols[i]+=1
                doPhrases(arr,cols,arrBool,output)
                cols[i]-=1
    
            return output 
    



 



arr=[['I','You','They'],['love','hate'],['food','games']]
print(phrases(arr))
 
