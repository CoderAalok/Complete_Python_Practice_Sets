def twosum(nums,k):
    seen = {} 
    for i ,val in enumerate(nums):
        diff = k - val 
        if diff in seen:
            return [seen[diff],i]
        seen[val] = i 
print(twosum([3,3],6))