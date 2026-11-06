GRAMS_PER_KILOGRAM = 1000

def main() -> None:
    kilos = int(input("Enter number of kilograms: "))

    grams= kilos * GRAMS_PER_KILOGRAM

    print(f"{kilos} kilograms is equal to {grams} grams")

if __name__ == "__main__":
    main()