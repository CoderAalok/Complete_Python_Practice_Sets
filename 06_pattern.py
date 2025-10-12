#solid Triangle

# size = 7
# for r in range(size):
#     for c in range(r,size):
#         print(' ',end='')
#     for c in range(r):
#         print('*',end='')
#     for c in range(r+1):
#         print('*',end='')
    
#     print()
    
#Solid Triangle
# size = 7
# for i in range(size):
#     for j in range(i,size):
#         print(' ',end='')
#     for j in range(i+1):
#         print('*', end=' ')
        
#        #Hollow triangle 
#         # if i == size-1 or j == i or j==0: 
#         #     print('*',end=' ')
#         # else:
#         #     print(' ',end=' ')
#     print()
    
# size = 7 
# for i in range(size):
#     for j in range(i+1):
#         print(' ',end='')
#     for j in range(i,size):
#         print('*', end=' ') #with space
#     # for j in range(i+1,size):#without space
#     #     print('*', end='')
    
#     print()

n = 5
for i in range(n):
    for j in range(n):
        if j == 0 or  i+j == n-1  or i == 0:
            print('*' , end=' ')
        else:
            print(' ', end=' ')
    print()