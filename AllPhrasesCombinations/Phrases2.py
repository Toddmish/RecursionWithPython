

def fromNext(arr,i=0, phrase=[]):
    if (i==len(arr)):
        return ['']
        
    remainedSentences=fromNext(arr,i+1)
    
    output=[]
    
    for word in arr[i]:
        for remainedSentence in remainedSentences:
            output.append(word+ ('' if (0==len(remainedSentence)) else ' ' )+ remainedSentence )
    return output
   

def phrases(arr):
    return fromNext(arr,0)
        
    
    

arr=[['I','You','They'],['love','hate'],['food','games']]

print(phrases(arr))