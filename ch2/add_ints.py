"""Add two integers"""

def main() -> None:
    """Διαβαζει δυο ακεραιους απο τον χρηστη τους προσθετει και εκτυπωνει το αποτελεσμα"""
    #Διαβαζουμε δυο ακεραιους απο τον χρηστη
    num1 = int(input("Enter first integer: "))
    num2 = int(input("Enter second integer: "))

    #Προσθεση των δυο ακεραιων
    result = num1 + num2

   #Εκτυπωση αποτελεσματος
    print(f"The sum of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()