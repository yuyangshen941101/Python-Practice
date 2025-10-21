#python 字串方法
# len() 、 find() 、 capitalize() 、 upper() 、 lower() 、 count() 、 replace()

#查詢字串方法 help(str)

# name = (input("你的名字"))

# L = len(name)
# print("您的全名一共有", L , "個字元")

# space = name.find(" ")
# print("你的空格在第", space , "個字元")

# capitalize的用法:統一名稱格式
# 當你處理使用者輸入（例如表單、註冊、資料庫）時，
# 可能有人輸入 aLiCe、ALICE、alice，
# 你可以用 capitalize() 統一成 Alice。
# capitalized = name.capitalize()
# print("你的名字第一個字母大寫" , capitalized)

# #replace
# phone_number = input("請輸入您的電話")
# phone_number = phone_number.replace("-", " ")
# print("您的電話號碼為:", phone_number)

Acc_name = (input("你的使用者名稱為:"))
if len(Acc_name) > 12:
    print("使用者名稱不可超過12個字元")
elif " " in Acc_name:
    print("使用者名稱中不可含有空格")
elif not Acc_name.isalpha():
    print("不可輸入數字")
else:
    print("您的使用者名稱為:", Acc_name)
