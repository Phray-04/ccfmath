"""【问题描述】
诚志小学即将举行跳绳比赛，看谁能在一分钟的时间内跳更多次。班主任老师让每一位同学回家
后要练习跳绳技能，练习后自己进行一次模拟比赛。
每天晚上学生要在微信群上报模拟比赛的成绩，格式为（学生姓名，成绩），其中成绩即为在一
分钟内跳了多少次。有的学生比较积极，每天都会进行练习并上报成绩，而有的学生则由于各种各样
的原因，并不是每天都能完成这项任务，甚至有的学生连一次成绩都没有上报。一周过去了，老师请
你帮忙编写一个程序，统计班级跳绳的最高成绩和最低成绩，以及参加了练习的学生人数。所谓参加
了练习的学生人数，就是说，如果某一位同学上报过一次或多次成绩，那么都计为一人。
【输入描述】
先输入一个正整数 N（其值不超过 100），接下来再输入 N 行，每一行是一个学生的一次成绩，
包括姓名和成绩。
【输出描述】
输出 √ 3 个正整数，表示最高成绩、最低成绩和参加练习的学生人数。
【输入样例】
√ 3
li 90
bai 95
li 98
【输出样例】
98 90 2
"""


def statistics(aTuple):
    scores = ()
    people = ()
    for t in aTuple:
        scores = scores + (t[1],)
        if t[0] not in people:
            people = people + (t[0],)
    max_s = max(scores)
    min_s = min(scores)
    Num = len(people)
    return max_s, min_s, Num


def main():
    N = int(input())
    records = ()
    for i in range(N):
        s = input().split(' ')
        r = (s[0], int(s[1]))
        records = records + (r,)
    (high, low, M) = statistics(records)
    print(str(high) + ' ' + str(low) + ' ' + str(M))


main()
