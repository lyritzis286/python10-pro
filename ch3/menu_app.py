"""Μενου επιλογών για την εφαρμογή με input choice και if-elif-else"""


def print_menu() ->None:
    print("Επιλέξτε μια επιλογή:")
    print("1. Κατάθεση")
    print("2. Ανάληψη")
    print("3. Υπολοιπο")
    print("4. Έξοδος")


def main() -> None:
    while True:
        print_menu()
        choice = input("Εισάγετε την επιλογή σας (1-4): ")

        if choice == "1":
            print("Επιλέξατε Κατάθεση")
            # Κώδικας για κατάθεση
        elif choice == "2":
            print("Επιλέξατε Ανάληψη")
            # Κώδικας για ανάληψη
        elif choice == "3":
            print("Επιλέξατε Υπολοιπο")
            # Κώδικας για εμφάνιση υπολοίπου
        elif choice == "4":
            print("Έξοδος από το πρόγραμμα.")
            break
        else:
            print("Μη έγκυρη επιλογή. Παρακαλώ δοκιμάστε ξανά.")




if __name__ == "__main__":
    main()