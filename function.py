def B(func):
    def C():
        print("so this?")
        func()
    return C

@B
def Add():
    print("B")

Add()