#巣狀迴圈

# for x in range(1,10):
#     print(x, end=" ")

# for y in range(5):
#     for x in range(1, 10):
#         print(x, end=" ")
#     print()

# row = int(input("輸入行數"))
# cols = int(input("輸入列數"))
# symbol = input("輸入符號")

# for i in range(row):
#     for j in range(cols):
#         print(symbol, end=" ")
#     print()

# list1 = [1, 2, 3]
# list2 = [3, 4, 5]

# for a in list1:
#     for b in list2:
#         if a == b:
#             print("重複:", a)

# for joint1 in range(0, 180, 30):  # 軸1角度
#     for joint2 in range(0, 180, 30):  # 軸2角度
#         print(f"模擬姿態：J1={joint1}, J2={joint2}") 用於動作路徑規劃、碰撞檢查、逆向運算。

# for i in range(num_sensors):
#     for j in range(num_actuators):
#         if sensor[i] > threshold[j]:
#             actuator[j].on()  
# 用來依照感測器狀態對應控制輸出，例如：
# 傳送帶系統多工位控制；
# 多組氣壓缸依序動作；
# 生產線自動檢測與分類。

from openpyxl import Workbook

# 建立 Excel 檔案
wb = Workbook()
ws = wb.active
ws.title = "測試資料"

# 巢狀迴圈填資料
for row in range(1, 6):        # 5 列
    for col in range(1, 11):   # 10 欄
        ws.cell(row=row, column=col, value=f"{row},{col}")

# 儲存檔案
wb.save("output.xlsx")
