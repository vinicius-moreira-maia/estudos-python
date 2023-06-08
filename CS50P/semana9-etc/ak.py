def f(*args, **kwargs):
    print(type(args), type(kwargs))
    print(args, kwargs)

f(1, 3, 2, 4, "xuxu", x = 32, y = 37)