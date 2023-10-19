"""
【问题描述】
输入一个字符串，该字符串只包含三种类型的字符：小写字母、大写字母和空格。然后将这个字
符串中的字符重新排列，生成一个新的字符串，即把所有的小写字母放在最前面，所有的空格放在中
间，所有的大写字母放在最后。而且这些小写、大写字母原来的顺序不能乱。最后把这个新的字符串
打印出来。
【输入描述】
输入一个字符串（长度不超过 100）
【输出描述】
输出字符重排列以后得到的新字符串。
【输入样例】
B a Ab
【输出样例】
ab BA（注意内部有两个空格）
"""
upper = ""
lower = ""
blank = ""
src = input()
N = len(src)
for i in range(N):
    if 'a' <= src[i] <= 'z':
        lower += src[i]
    elif 'A' <= src[i] <= 'Z':
        upper += src[i]
    elif src[i] == " ":
        blank +=src[i]

sub = lower + blank + upper
print(sub)

