def decorator_function(origin_function):
    def wrapper_function(*args, **kwargs):
        print('{}의 나이는 {}세입니다.'.format(*args, **kwargs))
        return origin_function(*args, **kwargs)

    return wrapper_function


@decorator_function
def origin_function(name, age):
    print('사실 {}의 나이는 {}세입니다.'.format(name, age))


origin_function('장비', 25)
