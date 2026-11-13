def factorial(n: int)-> int:
    result =1
    for i in range(1, n+1):
        result *= i
    return result

def main() -> None:
    """Κύρια συνάρτηση για την εκτέλεση του προγράμματος."""
    n = int(input("Δώσε έναν ακέραιο αριθμό για τον οποίο θέλεις να υπολογίσεις το παραγοντικό: "))
    result = factorial(n)
    print(f"Το παραγοντικό του {n} είναι: {result}")

if __name__ == "__main__":
    main()