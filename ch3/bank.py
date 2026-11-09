"""Αναληψη απο ATM """

EXIT_VALUE = 0
BANKNOTE = 20
BALANCE = 1000



def main() -> None:
    """Εκτελει αναληψεις ελεγχοντας τα error states"""
    initial_balance = BALANCE

    while True:
        print(f"Το υπολοιπο σας ειναι : {initial_balance}€")
        amount = int(input("Εισαγετε το ποσο που θελετε να αναληψετε (0 για εξοδο): "))

        if amount == EXIT_VALUE:
            print("Εξοδος απο το ATM")
            break

        if amount % BANKNOTE != 0:
            print(f"Λαθος ποσό. Μπορειτε να αναληψετε μονο πολλαπλασια του {BANKNOTE}€")
            continue

        if amount > initial_balance:
            print("Λαθος ποσό. Δεν εχετε αρκετα χρηματα στο λογαριασμο σας.")
            continue

        initial_balance -= amount
        print(f"Η αναληψη των {amount}€ ολοκληρωθηκε επιτυχως.")


if __name__ == "__main__":
    main()