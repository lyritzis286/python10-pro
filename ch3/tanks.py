"""Εφαρμογή δεξαμενών

- Πορτοκαλί = μια απο τις δυο ειναι κατω απο το οριο
- Κόκκινο = και οι δυο ειναι κατω απο το οριο

"""

LOW_LEVEL = 20

def main() -> None:
    """Διαβαζει τα επιπεδα δυο δεξαμενων και εκτυπωνει το χρωμα τους"""
    tank1 = 60
    tank2 = 15

    is_red_alarm = tank1 < LOW_LEVEL and tank2 < LOW_LEVEL
    is_orange_alarm = (tank1 < LOW_LEVEL) ^ (tank2 < LOW_LEVEL)

    print(f"Tank 1 level: {tank1}, Tank 2 level: {tank2}")
    print(f"Red alarm: {is_red_alarm}")
    print(f"Orange alarm: {is_orange_alarm}")


if __name__ == "__main__":
    main()


