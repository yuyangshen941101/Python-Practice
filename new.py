# 碼錶實作
import time

my_time = int(input("請輸入秒數"))

for x in range(my_time, 0, -1):
    # 02:00
    seconds = x % 60
    minutes = x // 60 % 60 # x / 60 的話會是浮點數 
    print(f"{minutes:02}:{seconds:02}") #02為取小數點後兩位
    # time.sleep(1) #暫停一秒再掃描
print("時間到了!")
