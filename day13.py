from collections import deque , _heapq

#Sample case -> nums[]
nums = [0,0,1,0,0,0,1,1]
arr = [-2]*(2*len(nums)+1)
arr[len(nums)] = -1
maxlen , count = 0, 0
for i in range(len(nums)):
    if nums[i]==0:
        count -= 1
    else:
        count += 1
    if arr[count+len(nums)] >= -1:
        maxlen = max(maxlen,i-arr[count+len(nums)])
    else:
        arr[count+len(nums)] = i

print(maxlen)



