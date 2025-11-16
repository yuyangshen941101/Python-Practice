#購物車
#list tuple set
items = []
prices = []

#無窮迴圈
while True:
    item = input("請輸入想購買的商品:")
    if item.lower() == "q":
        break
    
    price = float(input(f"請輸入{item}的價格:"))
    items.append(item)
    prices.append(price)
# print("商品:", items)
# print("價格:", prices)

for index, item in enumerate(items):
    print(f"第{index + 1}件 商品是 {item}, 價格:{prices[index]:.2f}")
    
total = sum(prices)
print(f"總價格:${total}")