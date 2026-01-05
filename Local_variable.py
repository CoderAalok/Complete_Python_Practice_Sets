x = 90
def local():
    print(x)#90
local()  #global variable read inside the function only
print(x) #90

x = 90
def local():
    x = 50
    print(x)  #50  same variable but different output->global can't be modify
local() 
print(x) #90
