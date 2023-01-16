def new_func():
    print("Hello World")


new_func()


def new_func_one(para):
    print("Hello World " + para)


new_func_one("Python")


def new_func_with_default_para(para="Python"):
    print("Hello World " + para)


new_func_with_default_para()
new_func_with_default_para("Java")


def new_func_unknown_para(*para):
    print("Hello World " + para[0])
    print("Hello World " + para[2])


new_func_unknown_para("Python", "Java", "C++")


def new_func_unknown_keyword_para(**para):
    print("Hello World " + para["name"])
    print("Hello World " + para["age"])


new_func_unknown_keyword_para(name="Python", keyword="language", age="Java")


def new_func_with_list(para):
    for i in para:
        print("Hello World " + i)


param = ["Python", "Java", "C++"]
new_func_with_list(param)


def new_func_with_return(para):
    return "Hello World " + para


new_func_with_return("Python")
new_func_with_return("Java")


def new_func_pass():
    pass


new_func_pass()


def new_func_recursive(n):
    if n == 0:
        print("Hello World")
        return 0
    else:
        print("Value of n is " + str(n))
        return n + new_func_recursive(n - 1)


new_func_recursive(10)
