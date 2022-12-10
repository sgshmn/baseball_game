import solve
from make import make_q


q = make_q()
print(q)

# print('>> 문제의 길이를 쓰세요')
# print('>> 2에서 8사이 숫자를 쓰면 돼요')
# al = int(input('>> '))  # answer length

al = 3

mn = 10 ** al  # max number
li = list(map(str, list(range(1, mn))))

for i, v in enumerate(li):
    li[i] = '0' * (al - len(v)) + v

rl = []  # remove list
for i, v in enumerate(li):
    if len(set(v)) < al:
        rl.append(v)

for i in rl:
    li.remove(i)

print(len(li))


while True:
    print('c >> continue')
    print('q >> quit')
    btn = input('  >> ')
    if btn == 'q':
        break

    elif btn == 'c':
        number = input('number >> ')
        s = int(input('s >> '))
        b = int(input('b >> '))
        sb = s + b

        li = solve.li_match_sb_nums(number, sb, li)
        li = solve.li_match_s_nums(number, s, li)
        for num_str in li:
            print(num_str, end=' ')
        print()
