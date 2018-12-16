# def max(a, b):
#     return a if a > b else b

# def the_max(x, y, z): # 函数的嵌套调用
#     c = max(x, y)
#     return max(c, z)

# print(the_max(1, 2, 3))



def outer():
    def inner():
        print('inner')
    inner()

outer()
















