#dic={}
#u=input("enter a language : ")
#q=input("enter a language : ")
#dic["L1"]= 1
#dic["L2"]= 2
#print(dic)

#a={"happy":"glad","nice":"great","cool":"clam"}
#print(tuple(a.keys()))
#u=input("Enter a basic word from above option :  ")
#z=a.get(u)
#print(z)

#a={"44",44}
#print(a)

#z=dict([("Hackathon","retrived data"),("api","npu")])
#print(z)

#dict={}
#dict.update({"competative":"programming", "hackathon":"project"})
#print(dict)

#f=input("name of fruit: ")

#a={"apple":("protein","vitamin", "calcium"),"banana":"healthy","dragon":"fruit"}

#z=a[f]
#print(z)
#print(a.items())
#print(a.get("coconut"))
#print(a["coconut"])


# dic = {
#     1:"red",
#     2:"Blue"
# }
# # del dic[1]  
# # out_of_range = dic.get(1, "No any specific color ")  #second argument work only when the inputed key not inside dictionary
# # print((out_of_range).title())

# li = []
# # dic = {'name':'****' , 'Address':"******" ,  'contact':'+98***'}  # constant and non-unique

# for i in range(2):
#     dic ={'name':'****' , 'Address':"******" ,  'contact':'+98***'}
#     n = input("Your name: ")
#     dic['name'] = n
#     a = input("Your address: ")
#     dic['Address'] = a
#     c = int(input("Your contact: "))
#     dic['contact'] = c 
#     li.append(dic)  #
# for j in li:
#     print(j)


# dic = {}
# i = 1 
# while i <= 2:
#     a = input("name: ")
#     b = input("AGE: ")
#     dic[a] = b
#     i += 1
# print(dic)   

# -------------------------------------------------------------
# Extract unique values from dictionary values list
# dic = {1:["Apple",'Banana','Coconut'] , 2:['Noodles','junks Food']}
# res = [x for val in dic.values() for x in val]
# print(res)


# def f(a,*b):
#     return a,b
# print(f((2,3,4,5),[5,3,2,6] , 1,'k',{8,0,0,8,7,6,7}))


# dic = {'dfcs':12, 'asd':2, 'okl':12}
# li = []
# dic1 = {}
# for s in sorted(dic.items()):
#     li.append(dict([s]))

# for i in li:
#     dic1.update(i)

# print(dic1)

# -------------------------------------------------------------
# Dictionary and counter in Python to find winner of election
# Method-I

# from collections import Counter

# def winner(li):
#     if not li:
#         return None

#     votes = Counter(li)

#     max_votes = max(votes.values())
#     candidates = list(votes.items())

#     max_res = [k for (k,v) in sorted(votes.items()) if v == max_votes ]

#     return (max_res[0],candidates,max_votes)

# li = ["john", "johnny", "jackie",
#     "johnny", "john", "jackie", "jamie", "jamie", "john",
#     "johnny", "jamie", "johnny","john"
# ]
# winCandidate,candidates,Maxvote = winner(li)
# print(f"The Winner of Election '{winCandidate}' with maximum votes:{Maxvote}")
# print()
# print(f"Join on Election Candidates are {candidates}")

# Method-II
# from collections import Counter

# def winner(li):
#     if not li:
#         return None

#     votes = Counter(li)
#     max_vote = max(votes.values())
#     Candidate = [names for (names,count) in sorted(votes.items()) if count == max_vote]
#     return  (votes,Candidate[0],max_vote)

# li = ["john", "johnny", "jackie",
#     "johnny", "john", "jackie", "jamie", "jamie", "john",
#     "johnny", "jamie", "johnny","john"
# ]
# Candidates,wincandidate,Maxvote = winner(li)
# print(f"The Winner of Election '{wincandidate}' with maximum votes:{Maxvote}")
# print()
# print(f"Join on Election Candidates are {Candidates}")

# -------------------------------------------------------------
# Append Dictionary Keys and Values ( In order ) in Dictionary
# Method-I
# li = [(1,'Lexicography'),(2,'Photogrophy'),(3,'Biology'),(4,'Technology')]
# dic = dict(li)
# dic[4] = 'Psychology'
# print(dic)

# # Method-II
# li_key = [1,2,3,4]
# li_val = ['Lexicography','Photogrophy','Biology','Technology']
# dic = dict(zip(li_key,li_val))
# print(dic)

# -------------------------------------------------------------
# Sort Python Dictionaries by Key or Value
# dic_items = {
#             "Apple":200,
#             "Dragan Fruit":1000,
#             "Kiwi":800,
#             "Banana":100
# }
# # According to Key make sort
# res = [k for k in sorted(dic_items.items())]
# print(dict(res))

# # According to Value make sort
# li = list(sorted(dic_items.items()))
# for i in range(1,len(li)):
#     if li[i][1] < li[i-1][1]:
#         z = li[i-1]
#         li[i-1] = li[i]
#         li[i] = z

# print(dict(li))
# ------------------------------------------------------------

# dic = {
#             "Apple":[300,200,250],
#             "Dragan Fruit":[1000,900,600],
#             "Kiwi":[1000,800,500],
#             "Banana":[250,800,100]
# }

# # Only Keys are sorted
# val = list(sorted(dic.items()))
# dic1 = dict(val)

# for i in dic1.keys():
#     dic1[i] = sorted(dic1[i])
# print(dic1)


# dic = {1:"Single", 2:"Multi", 3:"multiple"}
# print(dic.get(4,"Missing key"))

# user = 2
# if user not in dic:
#     print(f"{user} is missing key!")
# else:
#     print(dic[user])


# # Keys having multiple inputs means same value for all keys
# li = [(1,('Abstraction','Encapsulation','Inheritance')),(2,('Floppy Disk','SD Card','Hard Didk'))]
# li = [(('Abstraction','Encapsulation','Inheritance'),len(li[0][1])),(('Floppy Disk','SD Card','Hard Didk'),len(li[1][1]))]

# print(dict(li))

# # method-II
# dic = {}
# keys = ['Data','Resources','Storage','Documentation']
# res = dic.fromkeys(keys,"Networking")
# print(res)


# li = []
# for i in range(3,12):
#     li.append(i)
# li.append(1)
# print(sorted(li))
    
    # if li[len(li)-2]  == i:
    #     print(i,end=' ')


# liset = set()
# for i in range(5,10):
#     liset.add(i)
# liset.add(0)
# li = list(liset)
# print(li)


# K'th Non-repeates characters 

# from collections import Counter#OrderedDict 
# strr = "geeksforgeeks"
# q = 3

# # fre = OrderedDict()
# # for i in strr:
# #     fre[i] = fre.get(i,0) +1 #Accessing key it's value if exist else 0 get
# # print(fre)

# count = Counter(strr) #dictionary
# uniqueCharacter =''.join([k for k,v in count.items() if v == 1])
# uniqueLen = len(uniqueCharacter)
# if uniqueLen >= q:
#     print(uniqueCharacter[q-1:])
# else:
#     print(None)

# mid = len(uniqueCharacter)//2
# print(uniqueCharacter[mid])


#  Counter to find the size of largest subset of anagram words
# from collections import defaultdict
# def subset(strr):
#     if not strr:
#         return None
    
#     words = set(strr.split())
#     # dicSub = {} #default dictionary
#     dicSub = defaultdict(list)
#     for word in words:
#         key = ''.join(sorted(word))
#         # dicSub.setdefault(key,[]).append(word)

#         dicSub[key].append(word)
    
#     maxlenValue  = max(dicSub.values(), key=len)
#     return len(maxlenValue)

# strr = 'ant magnet magten manget tan heart earth'
# print(subset(strr))


# def sentences(strr):
#     if not strr:
#         return 
#     word = strr.split()
#     uniqueWord = []
#     for w in word:
#         if w not in uniqueWord:
#             uniqueWord.append(w)
    
#     print(' '.join(uniqueWord))

# strr = 'Python is good for beginner. Python is good for Artificial Inteligency'.strip()
# sentences(strr)


# li = ['microphone','telephone',
#       'cellphone','microphone',
#       'microchip','television',
#       'telephone','microphone'
#     ]

# count_frequency = {}
# for k in li:
#     if k not in count_frequency:
#         count_frequency[k] = 1
#     else:
#         count_frequency[k] += 1
        
# res = [k for (k,v) in count_frequency.items() if v>1]
# print(res)

# n = int(input())
# score = list(map(int,input().strip().split()))
    
# score = list(set(score))
# result = len(score)-2
# print(score[result])

# Dictionary to find mirror characters in a string
# ->  mirror characters are reverse of original alphabet order
# def mirror_characters(strr,N):
#     if strr.strip() == "" or N<0:
#         return None
    
#     alphachar = 'abcdefghijklmnopqrstuvwxyz'
#     revchar = alphachar[::-1]
    
#     dictchar = dict(zip(alphachar,revchar))  #dictionary create of mirror values
    
#     prefix = strr[:N-1]
#     surfix = strr[N-1:]
    
#     mirror = prefix
#     for i in range(len(surfix)):
#         mirror += dictchar[surfix[i]]
        
#     return mirror
# print(mirror_characters('zolp',1))



# li = [('python','pythonic'),('getter','setter')]
# print(dict(li))

# def frequency(li):
#     if not li:
#         return None
    
#     count = {}
#     for i in li:
#         count[i] = count.get(i,0)+1
#     re = [k for k,v in count.items() if v>1]
#     print(re)
# frequency(['getter','setter','getter','setter','decorator','wrap'])


# Counter and Dictionary Intersection Example (Make a string using deletion and rearrangement)
# from collections import Counter
# def count(s1,s2):
#     if s1.strip() == '' or s2.strip() == '':
#         return None
  
  
#     # return not(Counter(s1)-Counter(s2))#Working flow-> if s1 matches to all characters with s2 it become True(say:empty= False  so not(empty) that is  not(False)= True)
#     missing = Counter(s1) - Counter(s2)
#     return missing == 0
    # count_1 = Counter(s1)
    # count_2 = Counter(s2)
    
    # for k in count_1.keys():
    #     if count_1[k]  > count_2.get(k,0):
    #         return False
        
    # return True

    
    
    # Method-I
    # for ch in s1:
    #     if ch not in s2:
    #         return False
    # return True
    # Method-II
    # re = ["_"]*len(s1)
    # for i in range(len(s1)):
    #     for j in range(len(s2)):
    #         if s1[i] == s2[j]:
    #             re[i] = s2[j]
    #             break
    # return ''.join(re) == s1

# s1 ='Python'.lower()
# s2 = 'pytoafgfn'

# if all(s1 in s2 for s1 in s1):
#     print(f"It is possible to make {s1} word {s2}")
# else:
#     print(f"It is not possible to make {s1} word from {s2}")

# dictionary, set and counter to check if frequencies can become same

# from collections import Counter

# strr = "aabbb".lower()

# count = Counter(strr)
# freqs = list(count.values())
# unique = list(set(freqs))

# if len(unique) == 1:
#     print("YES! It can be possible")

# elif len(unique) == 2:
#     f,s = unique
    
#     high = max(f,s)
#     low = min(f,s)
    
#     # To check high frequency
#     if freqs.count(high) == 1 or high-1 == low:
#         print("YES! It can be possible")
#     else:
#         print("No! It can not be possible ")
        
# else:
#     print("No! It can not be possible ")
    
    
# Method: II

# from collections import Counter

# def possible_character(strr):
#     # if strr.strip() == "":
#     #     return None
    
#     count_freqs = Counter(strr)
#     li_freqs = list(count_freqs.values())
#     unique_freq = list(set(li_freqs))
    
#     if len(unique_freq) == 1:
#         return True
    
#     # Main condition
#     elif len(unique_freq) == 2:
        
#         high = max(unique_freq)
#         low = min(unique_freq)
        
#         # Counting possible frequencies
#         count_high = li_freqs.count(high)
#         count_low = li_freqs.count(low)
        
#         if (high -1 == low  and count_high == 1) or (low - 1 == 0 and count_low==1):  #frequencies
#             return True
        
#         else:
#             return False

#     else:
#         return False

# print(possible_character([0,1,0,1,0]))
# print(possible_character('abbccd'))
        




# d = {'Even':['0','2','4'], "Odd":['1','3','5']}
# val = list(d.values())
# for i in val :
#     print(i)

# print([i for i in val])

# print("  | ".join(d.keys()) )

""" Expected Output:
Even    Odd
0        1
2        3
4        5

"""

#first print keys
# for key in d.keys():
#     print(f"{key:<15}",end='')
# print()
# print("title\\author\\Status")
# #now print values
# for i in range(len(val[0])):
#     for value in val:
#         print(f" {value[i]:<15}",end='')
#     print()


dic = {1:{"title":["The Programmer","Re-searcher in AI"]},
       2:{"status":["available","unavailable"]}
    }


# dic = list(dic[1].keys())
# print(dic)
for i in range(1,len(dic)+1):
    
    for key in (dic[i].keys()):
        print(key)
        print("⁃"*8)
    
    
    
# re = dic[1]
# for key in re.keys():
#     print(f"{key:>10}",end=' ')
# print()

# for val in (list(re.values())[0]):
#     print(f"• {val:<15}")

# dic[len(dic)+1] = {'author':['Basant',"RD"]}