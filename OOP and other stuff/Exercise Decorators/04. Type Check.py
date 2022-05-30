def type_check(type_param):
    def decorator(function):
        def wrapper(num):
            if type_param == type(num):
                return function(num)
            return "Bad Type"

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))
