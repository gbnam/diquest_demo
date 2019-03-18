def decorator_function(origin_function):
    def wrapper_function(*args, **kwargs):
        print('{}의 나이는 {}세입니다.'.format(*args, **kwargs))

        return origin_function(*args, **kwargs)

    return wrapper_function


@decorator_function
def origin_function(name, age):
    print('사실 {}의 나이는 {}세입니다.'.format(name, age))


origin_function('장비', 25)

"""
1. 테스트할 때
2. 로그찍을 때
3. 로그인했을 때 로그인 계정 확인해서 계정에 해당하는 페이지로 리다이렉트
"""