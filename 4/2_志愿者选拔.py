"""
【问题描述】
学生志愿者选拔活动正在展开，首先进行笔试，笔试分数达到面试分数线的选手方可进入面试。
面试分数线根据计划录取人数的 150%划定，即如果计划录取 m 名志愿者，则面试分数线为排名
第 m×150%（向下取整）名的选手的分数，而最终进入面试的选手为笔试成绩不低于面试分数线的所
有选手。
现在就请你编写程序划定面试分数线，并输出所有进入面试的选手的报名号和笔试成绩。
【输入描述】
第一行两个整数 n，m(5≤n≤5000,3≤m≤n)，中间用一个空格隔开，其中 n 表示报名参加笔试的
选手总数，m 表示计划录取的志愿者人数。输入数据保证 m×150% 向下取整后小于等于 n。
第 二 行 到 第 n+1 行 ， 每 行 包 括 两 个 整 数 ， 中 间 用 一 个 空 格 隔 开 ， 分 别 是 选 手 的 报 名
号 k(1000≤k≤9999)和该选手的笔试成绩 s(1≤s≤100)。数据保证选手的报名号各不相同。
【输出描述】
第一行，有 2 个整数，用一个空格隔开，第一个整数表示面试分数线；第二个整数为进入面试的
选手的实际人数。
从第二行开始，每行包含 2 个整数，中间用一个空格隔开，分别表示进入面试的选手的报名号和
笔试成绩，按照笔试成绩从高到低输出，如果成绩相同，则按报名号由小到大的顺序输出。
【输入样例】
6 3
1100 85
1200 85
1009 90
1004 91
3927 92
8700 84
【输出样例】
85 5
3927 92
1004 91
1009 90
1100 85
1200 85
【样例说明】
m×150%=3×150%=4.5，向下取整后为 4。保证 4 个人进入面试的分数线为 85，但因
为 85 有重分，故最终有 5 个人进入面试。
"""
import math
from datetime import datetime

#将数字字符串列表转换为纯字符串列表
def to_int_list(lst):
    lst = lst.split()
