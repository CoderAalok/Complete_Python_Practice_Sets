# s = 'python'
# # for i in s:
# #     print(i)
# a = 'h'
# # # print(set(s))
# if a in s:
#     print(True)

# s = {1:2,3:4}
# a = min(s.values())
# print(a)


# s = 'python@'
# print(isinstance(s,str))
# print(s.isalpha())



# import string

# special = ";"
# if special in string.ascii_letters:
#     print("True")

# k = ""
# s = 'python'
# a = 'Encapsulation'
# for i,j in zip(a,s):  #python interpreter only minimum possible character print
#    k += i + j
   
# print(k)

# dic = {'s':3 , 'a':9 }
# a = max(dic.values())  #It gives maximum value
# a = max(dic, key = dic.get)  #It gives maximum value of its' key
# print(a)

# s= 's'
# print(s.isalpha())
# vars

# def f():
#     for i in range(10):
#         yield i+1  #yield function execute infinite time repeate single value but not itself  and itself resume

# for _ in range(3):
#     print(next(f()))

# Sum of all values 
# dic = {'Hard Disk':5000, 'RAM':2000, 'USE':1000}
# val = tuple(list(dic.values()))
# #Method-I
# print(sum(val))

# #Method-II
# sum_ = 0
# for i in val:
#     sum_ += i
# print(sum_)

# #Method-III
# addition = 0
# i = 0
# while i != len(val):
#     addition += val[i]
#     i += 1
# print(addition)


# OS = {'Floppy Disk': '500MB',
#       'Pen Drive':'32GB',
#       'CD/DVD': '1000MB',
#       'Smart Media': '256MB'
# }

# Method-I
# # del OS['Floppy Disk']
# print(OS)

# Method-II
# res = [[k,v] for k , v in OS.items() if v <'500MB']
# print(res)

# Method-III
# OS.pop('Floppy Disk')
# print(OS)
# add = (OS.get('Memory','Memory'))
# OS[add] = '16GB'
# print(OS)

# Method-I (Time Complexity: O(n))
# li = [{'Apple':300}, {'Banana':100}, {'Coconut':200}]
# for i in range(1,len(li)):
#     q,k = li[i-1] , li[i]
#     valQ = list(q.values())
#     valK = list(k.values())
#     if valK[0] < valQ[0]:
#         li[i],li[i-1] =li[i-1], li[i]
# print(li)

# Method-II
# List inside dictionaries using itemgetter 

# from operator import itemgetter

# Ways to sort list of dictionaries by values Using itemgetter

# li = [{"Name":"Walnut", "Price":1800},
#       {"Name":"Cashew", "Price":1500},
#       {'Name':'Apple','Price':300},
#       {'Name':'Banana','Price':100}, 
#       {'Name':'Coconut','Price':200}
#     ]
# result = sorted(li, key=itemgetter("Price"))
# print(result)
# ----------------------------------------------------------------

# Ways to sort list of dictionaries by values Using lambda function

# li = [{"Name":"Walnut", "Price":1800},
#       {"Name":"Cashew", "Price":1500},
#       {'Name':'Apple','Price':300},
#       {'Name':'Banana','Price':100}, 
#       {'Name':'Coconut','Price':200}
#     ]
# result = sorted(li, key=lambda i: i['Price'])
# print(result)
# -----------------------------------------------------------------

dict1 = {'Hacking':'Fishing', "Malicious":'Farewell'}  #dictionary itself negelete duplicate keys and values
dict2 = {"Malicious":'SwitchCase', "Interupt":'DATA'}
# Merging two Dictionaries
# Method-I
# dict1.update(dict2)
# print(dict1)

# # Method-II
# for key,value in dict2.items():
#     dict1[key] = value
# print(dict1)

# Method-III
# res = {**dict1,**dict2}
# print(res)

# # Method-IV
# result = dict1 | dict2
# print(result)
# ---------------------------------------------------

# Convert key-values list to flat dictionary
# li = list(dict1.items())
# # Method-I
# result = dict(li)
# print(result)

# # Method-II
# dic = {}
# for i in range(len(li)):
#     dic[li[i][0]] = li[i][1]
# print(dic)
# --------------------------------------------------

#Insertion at the beginning in OrderedDict
# Method-I (RAW logic)
# dic = {
#     "Linear Algebra":"Matrix",
#     "Calculas":"Differential Equation",
#     "Probability":"Statices"
# }
# l = len(dic)
# dic["Permutation"] = "Combination"
# dic.update({"Complex":"Cube Root", "Binomial Therome":"Mathematical Principal"})
# li = list(dic.items())
# print(li)
# res = li[l:] + li[:l]
# res = dict(res)
# print(res)

# Method-II
# from collections import OrderedDict

# dic = OrderedDict([("Linear Algebra","Matrix"),("Calculas","Complex Number")])
# dic.update({"Permutation":"Combination"})
# dic.move_to_end("Permutation",last=False)
# print(dic)

#Check order of character in string
# strr= "dettox"
# par = "tt"
# print(par in strr)

# def order(strr,pattern):
#     if not strr and not pattern:
#         return None
#     k = 0
#     for ch in strr:
#         if ch == pattern[k]:
#             k += 1
#             if k == len(pattern):
#                 return f"'{pattern}' character order matched in string '{strr}'."
#         else:
#             k = 0
#     return -1
# # Method-I
#     # T= 0
#     # for i in range(len(strr)):
#     #     if strr[i] == pattern[T]:
#     #         T += 1
#     #         if T == len(pattern):
#     #             return (f"'{pattern}' character order matched in string '{strr}'.")
#     #     else:
#     #         T = 0
#     # return -1
# strr= "detttox"
# pattern = 'at'
# print(order(strr,pattern))

# li = input().strip()
# print(li)

# li = [1,34,5,6,7]
# li.sort()
# li.pop(2)
# print(li)

# l = (input().strip())
# print()

# l = '2 0 4'
# a = (2,3,4)
# if all(int(i) in a for i in l.split() if i != '' ):
#     print(True)
# else:
#     print(False)

# n = int(input())
# t = tuple(map(int,input().strip().split()))

# print(hash(t))
# print(hash((1,2)))








# from itertools import permutations
# li = 'HACK'

# re = sorted(list(permutations(li,2)))
# print(re)
# result = [list(t) for t in re ]
# for ch in result:
#     print(''.join(ch))
# from itertools import permutations

# def arrange(strr,r=2):
    
#     re = sorted(list(permutations(strr,r)))
#     result = [list(i) for i in re]
    
#     for ch in result:
#         print(''.join(ch))

# strr= input().strip()


# arrange(strr,r) 

# s = map(input())
# print(s)
# strrInt = input().strip().split()
# print(strrInt)
# def permutation(arr):
#     # Base Condition
#     if not arr:
#         return []
    
#     if len(arr) <= 1:
#         return [arr]
    
#     # ---Main Approach---
#     result  = []
#     for i in range(len(arr)):
#         hold = arr[i]
#         rearrange = arr[:i] + arr[i+1:]
#         for ch in permutation(rearrange):
#             result.append(hold + ch)
#     return result

# print(permutation('asd'))


# def f(a):
#     c = list(range(len(a)))
#     c = list(range(3,0,-1))
#     return c
# print((f('asd')))    


# Dictionary to find mirror characters in a string
# def mirror(strr,n):
#     if strr.strip() == ""  or  n<0:
#         return None
    
#     alpha = 'abcdefghijklmnopqrstuvwxyz'
#     rev = alpha[::-1]
#     dictchar = dict(zip(alpha,rev)) #make dictionary of mirror characters both string
    
#     prefix = strr[:n-1]
#     surfix = strr[n-1:]
#     mirror = prefix
    
#     for i in range(len(surfix)):
#         mirror += dictchar[surfix[i]]
#     return mirror

# print(mirror('paradox',3))

# def mirror(strr,n):
#     if strr.strip() == ""  or  n<0:
#         return None
    
#     alpha = 'abcdefghijklmnopqrstuvwxyz'
#     rev = alpha[::-1]
    
#     prefix = strr[:n-1]
#     surfix = strr[n-1:]
    
#     mirror = str.maketrans(alpha,rev)
#     return    prefix + surfix.translate(mirror)
    
# print(mirror('paradox',3))
