"""varargs in python"""

def total(*numbers: float) -> float :
    """to numbers einai tuple"""
    return sum(numbers)


def main()-> None:
    print(total(1, 2, 3, 4, 5))
    print(total(10.5, 20.3, 30.2))
    print(total())

    nums = [1, 2, 3]
    print(total(*nums))

if __name__ == ("__main__:"):
    main()