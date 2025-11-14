# Number of test execute
t = int(input().strip())

for _ in range(t):
    N = int(input().strip())
    # k = int(input().strip())
    N -= 1
    
    def sumNumber(k):
        m = N//k
        ans = k*m*(m+1)//2
        return ans
    result = sumNumber(3) + sumNumber(5) - sumNumber(15)#->> twice avoid
    print(result)