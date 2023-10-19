# 研究生入学考试

n = int(input())
# 创建变量 n 存储输入数据并转换为整型
stu = [list(map(int,input().split())) for i in range(n)]
# 创建学生列表stu
# 用split将输入input的字符型数据分隔成每个单独项
# 用map将split分割好的每项字符串全转换成整型
# 用list将整个map整型数据转换成字符串格式的列表
stu = sorted(stu,key=lambda x:(-x[1], x[0]))
# 对stu 列表用sorted进行排序，定义key排序规则为lambda,首先降序排列-x[1]成绩，再升序排列成绩相同的
rank = 1

print(rank,stu[0][0],stu [0][1])

# 遍历
for i in range(1,n):
    if stu[i][1] != stu[i-1][1]:
        rank = i + 1
    print(rank,stu[[i][1])

# -----------------------------------------------------------------------------------


cdict = {}
# 用字典的键和值分别对应 ”汉字“ 和 ”汉字出现的次数“
for c in input():
    # for in 循环 用 c 遍历获取 input 用户输入的数据
    cdict[c] = cdict.get(c,0) + 1
#     c遍历时每出现一次就 +1

cnt = 0
# 提前设置一个统计数
for c in sorted(cdict,key=lambda x:cdict[x],reverse=True):
    # for in 循环用 c 遍历获取 sorted 方法对 cdict 排序的结果
    # key 的原本规则是以字典中 key 大小进行排序，要通过 lambda 函数表达式更改为以 value 大小进行排序
    # reverse 为 False 时升序，reverse 为 True 时降序

    print("{}:{:>5d}".format(c,cdict[c]))
    # 输出每个字符出现的次数作为结果，要保障字符宽度不大于五,使用 > 右对齐方法 小于5个字符;
    # 使用 format 两个占位符 绑定排序好的 c 键和值 ( c 就是键, cdict[c] 就是值)
    cnt += 1
    # 循环时每次 +1
    if cnt >= 10:
        # 只输出前十个，到第十个要 break 跳出循环
        break