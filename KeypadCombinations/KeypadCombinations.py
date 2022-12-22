# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")


map=["+", ".", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

'''
map=["+", ".", "ABC", "DEF", "GHI", "JKL",
             "MNO", "PQRS", "TUV", "WXYZ"]


map=["0":"+", 1:".", 2:"ABC", 3:"DEF", 4:"GHI", 5:"JKL",
             6:"MNO", 7:"PQRS", 8:"TUV", 9:"WXYZ"]
'''             
def keypadCombinations(keys,i=0,phrase=[], output=[]):
   
    if(i==(len(keys))):
        output.append(''.join(phrase))
    else:
        
        word=map[ int(keys[i]) ]
        #for j in range(0,len(word)):
        for ch in word:
            phrase.append(ch)
            keypadCombinations(keys,i+1,phrase,output)
            phrase.pop()
        
    return output
      

print(keypadCombinations('0'))
print(keypadCombinations('1')) #<- wrong result because it 
#contains the solution of the previous call


