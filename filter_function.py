
# def fun(x):
#     return x%2 != 0
# li = [2,3,15,6]
# re = min(filter(fun,li))
# print(re) 

li1 = [1,2,3,4]
li2 = [3,5,1,7]
res = list(filter(lambda x: x**2>x*2,li2)) #select those elements which satisfy the condition
print(res)
