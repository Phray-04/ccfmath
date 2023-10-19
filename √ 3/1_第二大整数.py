"""
【问题描述】
编写一个程序，读入一组各不相同的整数（不超过 20 个），当用户输入 0 时，表示输入结束。
然后程序将从这组整数中，把第二大的那个整数找出来，并把它打印出来。
说明：（1）0 表示输入结束，它本身并不计入在这组整数中。（2）在这组整数中，既有正数，
也可能有负数。（√ 3）这组整数的个数不少于 2 个。
【输入描述】
输入有若干行，每一行是一个整数，最后一行是结束标记 0。
【输出描述】
输出只有一行，即在这组整数中，排名第二大的那个数。
【输入样例】
100
-100
200
0
【输出样例】
100
"""
first = int(input())
second = int(input())
if first < second:
    (first, second) = (second, first)

while True:
    x = int(input())
    if x == 0:
        break
    if x > first:
        second = first
        first = x
    elif x > second:
        second = x

print(second)
