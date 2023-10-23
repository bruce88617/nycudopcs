"""
moduleZ of the "example2" package
"""


# absolute import
from example2.sub1.moduleX import sayHello2Y
from example2.sub2.moduleY import sayHello2X


def greeting():
    print("Someday, X meets Y...")
    print("X says: ", end="")
    sayHello2Y()
    print("Y says: ", end="")
    sayHello2X()
    print("The END")


