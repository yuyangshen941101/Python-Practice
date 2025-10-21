#體重轉換

w = float(input('請輸入體重'))
u = input("你的體重單位(kg/lb)").upper()

if u == 'KG':
    w *= 2.2
    new_u = '磅'
elif u == 'LB':
    w /= 2.2
    new_u = '公斤'
else:
    print('單位不正確')
    exit()

print(f'你的體重是 {round(w)} {new_u}')