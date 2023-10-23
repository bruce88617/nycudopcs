"""
Main scripts of the subpackage "sub1"
"""


# Absolute import
from sub1.moduleX import sayHello2Y, encounter
from sub2.moduleY import sayHello2X



if __name__ == "__main__":
    encounter()
    sayHello2Y()
    sayHello2X()


