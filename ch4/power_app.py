"""Calculate the power of a number."""

def power_calc(base: int, power: int) -> int:
    """Calculate the power of a number.

    Args:
        base (int): The base number.
        power (int): The exponent.

    Returns:
        int: The result of raising the base to the given power.
    """
    return base ** power

def main() -> None:
    base = int(input("Enter the base number: "))
    power = int(input("Enter the exponent: "))
    result = power_calc(base, power)
    print(f"{base} raised to the power of {power} is: {result}")

if __name__ == "__main__":
    main()