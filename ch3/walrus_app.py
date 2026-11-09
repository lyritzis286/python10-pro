"""Χρηση του walrus operator """


def main() -> None :
    count = 0

    while(num := int(input("Εισάγετε εναν ακεραιο αριθμό(>=0 για εξοδο): "))) < 0:
        count += 1

    print(f"Ο αριθμος των αρνητικων αριθμων που εισηχθησαν ειναι: {count}")


if __name__ == "__main__":
    main()
