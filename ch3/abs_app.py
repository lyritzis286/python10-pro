"""Απολυτη τιμη ενος ακεραιου με conditional expression"""


def abs_value(x: int) -> int:
    """Επιστρέφει την απόλυτη τιμή ενός ακέραιου αριθμού.

    Args:
        x (int): Ο ακέραιος αριθμός.

    Returns:
        int: Η απόλυτη τιμή του αριθμού.
    """
    return x if x >= 0 else -x

def abs_python(x: int) -> int:
    """Επιστρέφει την απόλυτη τιμή ενός ακέραιου αριθμού χρησιμοποιώντας τη συνάρτηση abs() της Python.

    Args:
        x (int): Ο ακέραιος αριθμός.

    Returns:
        int: Η απόλυτη τιμή του αριθμού.
    """
    return abs(x)


if __name__ == "__main__":
    num = int(input("Εισάγετε έναν ακέραιο αριθμό: "))
    print(f"Η απόλυτη τιμή του {num} είναι: {abs_value(num)}")
    print(f"Η απόλυτη τιμή του {num} (χρησιμοποιώντας abs()) είναι: {abs_python(num)}")