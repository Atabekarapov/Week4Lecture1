# def print_name():
#     print('Atabek')
# print_name()

# 2)
#  def print_name(name):
#     print(name)
# print_name('Atabek')

# 3)
# def add(num1, num2):
#     print(num1 + num2)
# add(7,9) #16

# 4)
# def add(num1, num2):
#     return num1 + num2
# result = add(4,6)
# print(result)

# 5)

# def summarize(a, b):
#     print(a + b)
# summarize(2,4)

# def summarize(*b):
#     print(sum(b))
# summarize(2,3,4)          ---> variant kogda my ne znayem imennogogo

# 6)
# def print_name(name = 'Atabek'):
#     print(name)                        -----> znachniye po umalchaniyu
# print_name('Beko')

# 7)
# def print_name(name = 'Atabek'):
#     print(name)                       
# print_name([1,2,3,4])         

# 8)
# def print_user(name = 'User', surname = 'UserSurname'):
#     print(name, '-', surname)
# print_user('Atabek')

# 9)
# def print_name(**name):
#     print(name)
# print_name(name = 'Bakyt')      --->unpacking sdeat imennovannymu

# 10)
# def print_name(name = 'User', surname = 'UserSurname'):
#     print(name, '-', surname)
# print_name(*args, **kwargs)

# 11)
# def foo(required, *args, **kwargs):
#     print(required)
#     if args:
#         print(args)
#     elif kwargs:
#         print(kwargs)
# foo('Privet', 1,2,3,4, key1 = 'Value1', key2 = 'Another value' )

# 12)
# result = lambda num1, num2: num1 + num2
# print(result(2, 5))

# 13)
# def func(a,b):
#     return a + b
# new_func = func
# print(new_func(3,4))

# 14)
# result = lambda num1, num2: print('Hello') if num1 > num2 else print('Bye')
# result(3,5)

# 15)
# def add(a, b):
#     return a + b
# print(add(2,3))













