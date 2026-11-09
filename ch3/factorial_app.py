"""Υπολογισμός του παραγοντικού ενός αριθμού"""

def factorial(n: int) -> int:
    """Υπολογίζει το παραγοντικό ενός αριθμού"""
    if n == 0:
        return 1

    i = 1
    result = 1
    while i <= n:
        result *= i
        i += 1
    return result

def main() -> None:
    """Διαβάζει έναν ακέραιο n από τον χρήστη και εκτυπώνει το παραγοντικό του"""
    n = int(input("Enter a non-negative integer n: "))
    if n < 0:
        print("Please enter a non-negative integer.")
        return

    result = factorial(n)
    print(f"The factorial of {n} is: {result}")

if __name__ == "__main__":
    main()
