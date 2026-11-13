
def power(base: int, exponent: int) -> int:
    result = 1
    for _ in range(exponent):
        result *= base
    return result

def main() -> None:
    """Κύρια συνάρτηση για την εκτέλεση του προγράμματος."""
    base = int(input("Δώσε τη βάση: "))
    exponent = int(input("Δώσε τον εκθέτη: "))
    result = power(base, exponent)
    print(f"{base} υψωμένο στη δύναμη {exponent} είναι: {result}")

if __name__ == "__main__":
    main()