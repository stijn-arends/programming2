
def simple_sum(a, b):
    return a + b


def multiple_sum(*args):
    parameters = args
    print(parameters)
    sm = 0
    for param in parameters:
        sm += param

    return sm