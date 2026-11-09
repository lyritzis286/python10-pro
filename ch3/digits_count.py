
def count_digits(n: int) -> int:
    tmp = abs(n)
    digits = 0
    while True:
        digits += 1
        tmp //= 10
        if tmp == 0:
            break
    return digits


def main() -> None:
    num = int(input("Εισαγετε εαν ακεραιο "))
    print(f"Ο αριθμος των ψηφιων του {num} ειναι : {count_digits(num)}")


if __name__ == "__main__":
    main()