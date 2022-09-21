# Main scripts of the "example1" package

# Absolute import
from example1.module1 import hello
from example1.module2 import youfool


# # Relative import
# from .module1 import hello
# from .module2 import youfool


if __name__ == "__main__":
    hello()
    youfool()

