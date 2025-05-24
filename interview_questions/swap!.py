"""swap without swap! for fun"""


def swap(a, b):

    a = a + b
    b = a - b
    a = a - b

    return a, b