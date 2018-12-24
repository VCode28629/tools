if __name__ == '__main__':
    f = open('problems.txt', 'r', encoding='UTF-8')
    ans = []
    for str in f.readlines():
        str = str.split()
        if len(str) == 0:
            continue
        if str[0][0] == 'P':
            ans.append(int(str[0][1:]))
        if len(str) == 1:
            continue
        elif str[1][0] == 'P':
            ans.append(int(str[1][1:]))
    f.close()
    f = open('ans.txt', 'w')
    for item in ans:
        if item == ans[-1]:
            print(item, file=f)
        else:
            print('{},'.format(item), file=f, end=' ')
    