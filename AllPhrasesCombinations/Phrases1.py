

def phrases(arr):
	
		
	allPhrases=[]
	
	def createPhrases(arr,i=0, phrase=[]):
		
		if (i==len(arr)):
			allPhrases.append(' '.join(phrase))
			return
	
		for word in arr[i]:
			phrase.append(word)
			createPhrases(arr,i+1,phrase)
			phrase.pop()
	
	createPhrases(arr)

	return allPhrases

arr=[['I','You','They'],['love','hate'],['food','games']]

print(phrases(arr))