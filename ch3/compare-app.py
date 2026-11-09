"""Αλυσιδοτες συγκρισεις."""

MIN_GRADE = 50
MAX_GRADE = 100

def is_passing(grade: int) -> bool:
    """Επιστρέφει True αν η βαθμολογία είναι επιτυχής βρισκεται μεταξυ 50-100."""
    return MIN_GRADE <= grade <= MAX_GRADE

def main() -> None:
    """Ελέγχει αν οι βαθμολογίες είναι επιτυχείς."""
    for grade in(80, 90, 40, 30):
        is_grade_passing = is_passing(grade)
        print(f"Grade: {grade}, Passing: {is_grade_passing}")

    print()

if __name__ == "__main__":
    main()