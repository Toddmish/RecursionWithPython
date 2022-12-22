
def doKeypadCombinations(keys,i=0, map = ["+", ".", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"],phrase=[], output=[]):
   
    if i==len(keys):
        output.append(''.join(phrase))
    else:
        
        word=map[ int(keys[i]) ]
        #for j in range(0,len(word)):
        for ch in word:
            phrase.append(ch)
            doKeypadCombinations(keys,i+1,map,phrase,output)
            phrase.pop()
        
    return output
    
def keypadCombinations(keys):
    map = ["+", ".", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
    return doKeypadCombinations(keys,0,map,[],[])
    
print(keypadCombinations('0'))
print(keypadCombinations('1'))
print(keypadCombinations('29'))