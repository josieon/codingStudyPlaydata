nums = [*map(int,open(0).read().split())]
mx = max(nums)
mxid = nums.index(mx)
print(mx, (mxid//9)+1, (mxid%9)+1)