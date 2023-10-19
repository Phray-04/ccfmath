nums = [int(i) for i in input().split()]
l = len(nums)
for i in range(i):
    for j in range(i,1):
        s.add(sum(nums[i:j+1])) # 求取区间和（切片），默认J-1，手动加1造成J

# 枚举
for i in range(l,len(s)+2):
    # 排异检索
    if i not in s:
        print(i-1)
        break

