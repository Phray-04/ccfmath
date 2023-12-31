"""
【问题描述】
一位考古科学家新发掘了一批恐龙蛋化石，假设有 N 个，编号分别为 1～N，然后打算对它们进
行研究。在科学家的实验室里，有两间房间，一间是他的办公室，一间是储物间。开始时所有的恐龙
蛋化石都摆放在储物间，然后需要用到哪一个的时候，就把它拿到办公室来。在科学家的办公室有一
张办公桌，桌上有 M 个盘子，如 4 个盘子，每个盘子只能摆放一个恐龙蛋化石。科学家在进行研究时，
时而要研究这个，时而要研究那个，因而有一个编号序列，如 1 2 5，就是先研究 1 号化石，再研究
2 号，再研究 5 号。如果科学家需要研究某一个化石的时候，该化石正好就在办公桌的某个盘子里，
那么就直接研究即可；如果该化石不在办公桌上，我们称这种情形为“缺蛋”，这时就需要站起身，
去一趟隔壁的储物间，把想要的化石拿过来。但这么做有一个前提，就是办公桌上必须有空盘子，如
果有空盘子，就可以把取来的化石放在某个空盘子里；而如果没有空盘子，就必须先把某一个盘子中
的化石放回到储物间，从而腾出空间，然后才能把新的化石放进去。但问题是，桌子上有 M 个盘子，
那么选择哪一个盘子中的化石，把它放回去（我们称为淘汰），这是需要仔细考量的。如果放回去的
化石，过一会儿又要用到，那么就又得跑一趟储物间，这就浪费时间了。因此，一个朴素的想法就是
哪一个化石将来不会再用上，就把该化石拿走。但问题是，科学家自己也不知道将来会用到哪一个化
石，换言之，他在做研究的时候是天马行空，想到哪儿是哪儿，因此他只知道自己当前需要用到哪一
个化石，而将来的情形则不知道。在这种情形下，如何来做出比较好的淘汰决策呢？
为了减少“缺蛋”的次数，他向一位计算机科学家寻求帮助，计算机科学家向他推荐了 LRU（Least
Recently Used）算法。该算法的基本思路是，虽然将来的情形我们是不知道的，但是过去的情形是
知道的，因此我们可以根据过去的情形来预期将来的情形。具体来说，如果在过去一段时间内，某个
化石刚刚被用到，那么在将来一段时间内，它也很可能会再次被用到；反之，如果在过去一段时间内
某个化石很久没有被用到，那么将来它也可能很久不会被用到。因此可以利用这个信息来进行淘汰。
举个例子，假设科学家研究的编号序列为 1、2、3、4、1、2、5、1、2、3、4、5（这个编号序
列是事后统计出的），盘子的个数为 4，初始为空，那么采用 LRU 算法，总共会“缺蛋”8 次。即在
访问最前面的 1、2、3 和 4 时，都会“缺蛋”，需要去一趟储物间。但此时由于有空闲的盘子，所以
取来化石后都能直接摆进去，不需要淘汰某个化石。然后在访问接下来的 1 和 2 时，由于这两个化石
已经在盘中，所以不会“缺蛋”。接下来在访问 5 号化石时，此时它不在办公桌上，然后桌上也没有
空盘子了（分别装了 1、2、3 和 4 号化石），所以先要选择某个化石淘汰，根据 LRU 算法，在当前时
刻，2 号是最近刚访问过的，所以要保留，1 号和 4 号其次，而 3 号是最久以前访问过的，所以就淘
汰 3 号化石，把它放回到隔壁的储物间，然后把 5 号化石放到桌上的空盘里。后面是类似的，接下来
的 1 和 2 不会“缺蛋”，而最后的 3、4 和 5 都会“缺蛋”，所以总共“缺蛋”8 次。
【输入描述】
输入有两行，第一行是一个正整数 M，表示盘子的个数，其值不超过 100。第二行是一个编号序
列。
【输出描述】
输出一个正整数，表示“缺蛋”的次数。
【输入样例】
4
1 2 √ 3 4 1 2 5 1 2 √ 3 4 5
【输出样例】
8
"""
def main():
    FN = int(input())
    s = input()
    pages = s.split(' ')
    for i in range(len(pages)):
        pages[i] = int(pages[i])

    FaultNum = 0
    list = []

    for p in pages:
        if p in list:
            i = list.index(p)
            element = list.pop(i)
            list.append(element)
        else:
            FaultNum += 1
            list.append(p)
            if len(list) > FN :
                del(list[0])
    print(FaultNum)


main()