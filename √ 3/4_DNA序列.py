def main():
    N = int(input())
    DANs = []
    for i in range(N):
        dna = input()
        DANs.append(dna)
    length = len(DANs[0])
    result = ''

    for j in range(length):
        num = [0.3, 0.2, 0.1, 0]
        for i in range(N):
            if DANs[i][j] == 'A':
                num[0] += 1
            elif DANs[i][j] == 'C':
                num[1] += 1
            elif DANs[i][j] == 'G':
                num[2] += 1
            elif DANs[i][j] == 'T':
                num[3] += 1
        jianji = ['A', 'C', 'G', 'T']
        max = 0
        for i in range(4):
            if num[i] > max:
                max = num[i]
                c = jianji[i]
        result += c
    print(result)


main()
