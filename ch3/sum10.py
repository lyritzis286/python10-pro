"""Υπολογισμός του αθροίσματος των n πρωτων φυσικών αριθμών"""

def sum_first_n(n: int) -> int:
    """Υπολογίζει το άθροισμα των n πρώτων φυσικών αριθμών"""
    # return n * (n + 1) // 2
    total_sum = 0
    i =1
    while i <= n:
        total_sum += i
        i += 1

    return total_sum

def main() -> None:
    """Διαβάζει έναν ακέραιο n από τον χρήστη και εκτυπώνει το άθροισμα των n πρώτων φυσικών αριθμών"""
    n = int(input("Enter a positive integer n: "))
    if n < 1:
        print("Please enter a positive integer.")
        return

    result = sum_first_n(n)
    print(f"The sum of the first {n} natural numbers is: {result}")

if __name__ == "__main__":
    main()