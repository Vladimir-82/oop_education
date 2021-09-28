'''
Exclamation marks series
'''
def convert(s):
    num = ''
    flag = s[0]
    counter = 0
    for i in s:
        if i == flag:
            counter += 1
        else:
            num += str(counter)
            counter = 1
            flag = i
    num += str(counter)
    num = int(num)

    i = 2

    if num == 2:
        return 2

    while True:
        if not num % i:
            num = num // i
            i = 2
        else:
            i += 1
        if i == (num - 1) or i == num:
            return num

print(convert("!!!"))

