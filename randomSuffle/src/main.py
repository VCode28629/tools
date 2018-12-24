import random
if __name__ == '__main__':
    f = open('problems.txt', 'r', encoding='UTF-8')
    ans = []
    for str in f.readlines():
        ans.extend(str.split())
    random.shuffle(ans)
    
    f.close()
    f = open('ans.txt', 'w')
    for item in ans:
        if item == ans[-1]:
            print(item, file=f)
        else:
            print('{},'.format(item), file=f, end=' ')
    