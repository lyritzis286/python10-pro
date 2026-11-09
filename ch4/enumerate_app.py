NAMES = ("ANNA", "BILL", "CHARLIE")
GRADES = (85, 92, 78)

def main() -> None:
    print("Χρηση της enumerate():")
    for index, name in enumerate (NAMES, start = 1):
        print(f"{index}: {name}")

    print("\nΧρηση της zip():")
    for name, grade in zip(NAMES, GRADES, strict=True):
        print(f"{name}: {grade}")

    total = 0
    for grade in GRADES:
        total += grade
    print(f"\nΜεσος ορος βαθμολογιας: {total / len(GRADES):.2f}")



if __name__ == "__main__":
    main()