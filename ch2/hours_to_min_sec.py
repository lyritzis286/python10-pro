"""Convert hours to minutes and seconds"""


MINUTES_PER_HOUR = 60
SECONDS_PER_MINUTE = 60

def main() -> None:
    """Convert hours to minutes and seconds"""
    #Data input
    hours = int(input("Enter number of hours: "))

    #Processing
    minutes = hours * MINUTES_PER_HOUR
    seconds = minutes * SECONDS_PER_MINUTE

    #Output
    print(f"{hours} hours is equal to {minutes} minutes or {seconds} seconds)")

if __name__ == "__main__":
    main()