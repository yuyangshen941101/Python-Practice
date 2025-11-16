# list 是有序且可變的集合，適用於需要保持順序並且可能需要修改的數據。
# tuple 是有序且不可變的集合，適用於不需要修改的數據。
# set 是無序且元素唯一的集合，適用於需要去重或進行集合運算的數據。

# fruits = ["A", "B", "C", "D"]

# print(fruits[0]) # 搜尋第0個元素

# for f in fruits:
#     print(f) 

# fruits.append("E") #加入元素並放置在最後一位
# print(fruits)

# fruits.remove("A")
# print(fruits)

# print(fruits.index("C"))

# fruits.append("A") #假設是在遊戲當中的話，這種指令應該可以作為新增一個物件的那種指令。
# fruits.append("A")
# print(fruits)

# print(fruits.count("A"))

# print(fruits)
# fruits.reverse() #反轉列表順序
# print(fruits)

# set 一種東西只會存在一個
fruits_set = {"😊","🤣","😂"}
fruits_set.add("❤️") 
# fruits_set.add("😂")
# for fruit in fruits_set:
#     print(fruit, end=" ")
if "😂" in fruits_set:
    print("有一個笑臉")
    
# if "❤️" in fruits_set:
#     print("有一顆愛心")
# else:
#     print("沒愛心")

# tuple 元組
# fruit_tuple = ("❤️","🤣","😊","❤️")
# result = fruit_tuple.count("❤️")
# # result = fruit_tuple.index("❤️")
# # fruit_tuple.add("❤️")
# print(result)