
from forward_operator import * 
from operator/cfa_operator import * 

def main():
    # creation of forward operator
    cfa_op = cfa_operator('bayer_bis', (50, 50, 10), ?, 'dirac')

    # not needed for now ! 
    # operator = forward_operator(operator_list=["cfa_operator"])
    print("test")


if __name__ == '__main__':
    # Execute when the module is not initialized from an import statement.
    main()