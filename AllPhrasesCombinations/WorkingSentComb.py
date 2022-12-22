'''
an unnecessarily complicated solution

cols[i] holds the current position for the i-th row of the input

In current example len(cols)==3
 
'''
def doPhrases(arr,cols, output =[] ):

    beyond=False
    for i in range(0,len(arr)):
        if(cols[i]>=len(arr[i])):
            beyond=True
    
    if (True==beyond):
        return 
        
    else:
        #any sentence will start with a word from the first row of the input
        #cols[s] holds currrent the position in the first row
        sentence= arr[0][cols[0]]
        
        for i in range(1,len(cols)):
            sentence+=" "+ arr[i][cols[i]]
        
        if not sentence in output:
            output.append(sentence)
            print(sentence)
        
       
        for i in range(0,len(arr)):
            cols[i]+=1
            doPhrases(arr,cols,output)
            cols[i]-=1
        return output 
    


arr=[['I','You','They'],['love','hate'],['food','games']]

def phrases(arr):
    zeros=[0  for i in range(0,len(arr))]
    return doPhrases(arr,zeros,[])

print(phrases(arr))