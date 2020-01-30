def my_func(first, second, third):
    if first >= third and second >= third:
        return first + second
    elif first >= second and third >= second:
        return first + third
    else:
        return second + third

