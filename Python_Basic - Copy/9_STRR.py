strr1 = ("Large Language Model Used For Web Application").split() 
strr2 = ("Large Diffusion Model") 
print("Uncommon words are found from strr1: ") 
for i in strr1 : 
    if not i in strr2: 
        print(i,end='->') 
    else: continue