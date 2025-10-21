#運算符號 (運算子)

#and or not

temp = int(input("輸入目前溫度"))
#if temp > 0 and temp < 30 :
#    print("溫度適宜")
#else:
#    print("溫度不適")

if temp >= 30 or temp <= 0:
    print("溫度不適")
else:
    print("溫度合適")