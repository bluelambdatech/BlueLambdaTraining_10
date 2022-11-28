
def add(x, y):
    """
    This function is used to add two numbers
    :x: int -> first number to add
    :y: int -> second number to add
    return: int -> addition of x and y

    Example: if x = 10 and y = 15, then the function returns 25
    """
    return x + y


def minus(x, y):
    return x - y


multiply = lambda x, y, z: 2 * x * y * z

# Classes


class Maths:
    name = 'Edward'

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def minus(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def add_minus(self):
        minu = self.minus()
        ad = self.add()
        return minu, ad



ma = Maths(3, 2)
print(ma.add_minus())
