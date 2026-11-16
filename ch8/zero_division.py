import logging

logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s - [%(levelname)s] %(name)s: %(message)s",
    datefmt = "%Y-%m-%d %H:%M:%S")

logger  = logging.getLogger(__name__)
def div(a: int, b: int) -> int | None   :
    try:
        return a// b
    except ZeroDivisionError as error:
        logger.warning(f"Σφαλμα: δεν μπρει να γινει διαιρεση με το μηδεν λεποτμερειες {error}")
        raise

def main() -> None :
    a = 10
    b = 0

    try:
        result = div(a,b)
    except ZeroDivisionError:
        print("Σφαλμα δεν μπορει να γινει διαιρεση με το μηδεν")
    else:
        print(f"to apotelesma einai {result}")

if __name__ == "__main__":
    main()