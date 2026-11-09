"""Εμφανιση 10 αστεριων στο τερματικο"""

STARS = 10

def main() -> None:

    i = 1
    while i <= STARS:
        print("*", end="")
        i += 1
    print()

    j = STARS
    while j >= 1:
        print("*", end="")
        j -= 1
    print()


if __name__ == "__main__":
    main()