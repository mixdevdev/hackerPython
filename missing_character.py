import string
import random
def missingCharacters(s):
    all_number=[]
    all_aphabet=[]
    temp_list=[]
    final=''

    alphabet = string.ascii_lowercase
    for i in range (0,10):
        all_number.append(str(i))
    # print (type(all_number[0]))
    for i in alphabet:
        all_aphabet.append(i)
    # import pdb; pdb.set_trace()
    for i in s:
        if i in all_aphabet:
            all_aphabet.remove(i)
        if i in all_number:
            all_number.remove(i)
    # print (temp_list)
                
    
    b=all_number+all_aphabet
    print (all_number)
    final=''.join(str(item) for item in b)
    return final
    
        
    

print(missingCharacters('8hypotheticall024y6wxz'))