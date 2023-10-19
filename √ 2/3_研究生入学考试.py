# 解法2
# 转换成数字，将数字翻转（/保留小数除法。//整除不保留小数）
# 取个位数再输出个位数

num2 = int(input())
num3 = 0
while num2 > 0 :
    # num2 = num2*10 + num2 % 10
    print(num2 % 10,end="")
    num2 = num2 //10

#     -----------------------------------------------------------------------------

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

