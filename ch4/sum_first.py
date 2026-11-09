"""Sum the first n natural numbers."""


def sum_first_ints(n: int) -> int:
    total_sum = 0
    # for i in range(1, n + 1):
    #     total_sum += i
    for i in range(n):
        total_sum += i + 1
    return total_sum


def multiply_first_ints(n: int) ->int:
    product = 1
    for i in range(1, n+1):
        product *= i
    return product

def main() -> None:
    n = int(input("Enter a positive integer n: "))
    if n < 1:
        print("Please enter a positive integer.")
        return

    sum_result = sum_first_ints(n)
    product_result = multiply_first_ints(n)
    print(f"The sum of the first {n} natural numbers is: {sum_result}")
    print(f"The product of the first {n} natural numbers is: {product_result}")




if __name__ == "__main__":
    main()


