def Reverse(string):
    result = []
    for i in string.split()[::-1]:
        result.append(i[::-1])
        
    return" ".join(result)

string = "i am testing"
print(Reverse(string))             
    
    
