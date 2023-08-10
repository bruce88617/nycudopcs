# Main scripts of the subpackage "sub2"
# Absolute import
from sub2.moduleY import sayHello2X, encounter
from sub1.moduleX import sayHello2Y


if __name__ == "__main__":
    encounter()
    sayHello2X()
    sayHello2Y()


