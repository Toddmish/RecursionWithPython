def fromNext(keys,i,map):
    
    if(i>=len(keys)):
        return ['']
    
    else:
        keypad=map[int(keys[i])]
        combinations=fromNext(keys,i+1,map)
        output=[]
        for ch in keypad:
            for ele in combinations:
                output.append(ch+ele)
        return output
    


def keypadCombinations(keys):
    map = ["+", ".", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
    return fromNext(keys,0,map)

    
print(keypadCombinations('0')) 
print(keypadCombinations('1')) 
print(keypadCombinations('29')) 
