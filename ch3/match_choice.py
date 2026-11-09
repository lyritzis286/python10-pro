"""Match choice implementation"""


def decide_on_choice(choice: str) -> str:
    """Decide on a choice using match-case statement."""
    match choice:
        case "1":
            return "You chose rock. It's a solid choice!"
        case "2":
            return "You chose paper. It can cover rock!"
        case "3":
            return "You chose scissors. It can cut paper!"
        case _:
            return "Invalid choice. Please choose 1, 2, or 3."