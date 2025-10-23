def uncommon(strr1,strr2):
    if strr1 == '' or strr2 == '':
        print("String is blank")
    words = []
    words_1 = strr1.split()
    words_2 = strr2.split()
    for w in words_1:
        if w not in words_2:
            words.append(w)
    return words
strr1 = "Protocol is rulebook for communication between devices on internet"
strr2 = "HTTP is a Protocol , which communication to the server in such a way"
print(uncommon(strr1,strr2))