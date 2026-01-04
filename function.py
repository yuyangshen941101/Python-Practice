# def B(func):
#     def C():
#         print("so this?")
#         func()
#     return C

# @B
# def Add():
#     print("B")

# Add()
# 方法(method) 函式(function)

# def say_hello():
#     print("Hello")

# say_hello()

# 傳遞參數

# def greet(name):
#     print(f'Hello, {name}!')
# greet("帥哥")

def add(x,y):
        return x + y
result = add(3,5)
print(result)  # 輸出: 8

def sub(x,y):
        return(x - y)
result1 = sub(10,4)
print(result1)  # 輸出: 6

def mul(x,y):
        return(x * y)
result2 = mul(2,6)
print(result2)  # 輸出: 12

def dev(x,y):
        return(x/y)
result3 = dev(3,2)
print(result3)  # 輸出: 1.5

def create_name(fir ,last):
    fir = fir.capitalize()
    last = last.capitalize()
    return fir + "" + last

print(create_name("tony","stark"))