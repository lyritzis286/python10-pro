"""Truthiness in Python."""

FALSE_VALUES = (None, 0, 0.0, '', [], {}, set())
TRUTHY_VALUES = (True, 1, -1, 0.1, 'Hello', " ", [1], {1: "One"}, {1})


def main() -> None:
    print("Falsy values:")
    for value in FALSE_VALUES:
        print(f"{value!r} is falsy: {bool(value)}")

    print("\nTruthy values:")
    for value in TRUTHY_VALUES:
        print(f"{value!r} is truthy: {bool(value)}")


if __name__ == "__main__":
    main()