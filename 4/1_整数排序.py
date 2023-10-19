"""
【问题描述】
老师给定 10 个整数的序列，要求对其重新排序。排序要求:
1.奇数在前，偶数在后；
2.奇数按从大到小排序；
3.偶数按输入顺序逆序排序。
【输入描述】
输入一行，包含 10 个整数，彼此以一个空格分开，每个整数的范围是大于等于 0，小于等于 100。
【输出描述】
按照要求排序后输出一行，包含排序后的 10 个整数，数与数之间以一个空格分开。
【输入样例】
4 7 3 13 11 12 0 47 34 98
【输出样例】
47 13 11 7 3 98 34 0 12 4
"""
from datetime import datetime

string = input("please input 10 num:")

l = string.split()
for i in range(10):
    l[i] = int(l[i])
print(l)

starttime = datetime.now()

oushu = []
jishu = []
for i in l:
    if i % 2 == 0:
        oushu.append(i)
    else:
        jishu.append(i)

print(jishu.sort(reverse=True))
print(list(reversed(oushu)))

endtime = datetime.now()
print(jishu + list(reversed(ou)),"用时：{:.5f}".format((endtime-starttime)))