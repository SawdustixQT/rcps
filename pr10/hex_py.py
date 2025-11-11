def hex2(a):
    res = ''
    hex_str = '0123456789ABCDEF'
    while a > 0:
        ost = a % 16
        res += hex_str[ost]
        a //= 16
    res = '0x' + res[::-1]
    print(res)
    
def min2(lst):
    res = lst[0]
    for i in lst:
        if i < res:
            res = i
    print(i)

hex2(25)
    
