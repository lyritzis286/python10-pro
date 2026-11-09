def main() -> None:
    count = 0

    num = int(input("Enter a number (>0 to stop): "))
    while num <0 :
        count += 1
        num =int(input("Εισαγετε εναν ακεραιο αριθμο(>0 για εξοδο))"))

    print(f"Ο αριθμος των αρνητικων που εισηχθησαν ειναι : {count} ")

if __name__ == "__main__":
    main()