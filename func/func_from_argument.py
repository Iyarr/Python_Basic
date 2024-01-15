def mul_func(a,b):
    return a * b

def div_func(a,b):
    return a / b

def calc_5_3(func):
    return func(5,3)

func = div_func
result = func(2,3)
print(result)

func = mul_func
result = func(10,5)
print(result)

result = calc_5_3(mul_func)
print(result)