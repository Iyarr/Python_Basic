def named_func():
    print("this func is named")

no_name = lambda : print("this func is not named")

no_name_multiple_process = lambda : (print("this process is 1"),print("this process is 1"))

no_name_with_argument = lambda x : print(f"my breakfast is {x}")

named_func()
no_name()
no_name_multiple_process()
no_name_with_argument("TKG")

nums = range(1,6)
x2 = lambda x : x*2
nums = list(map(x2,nums))
print(nums)