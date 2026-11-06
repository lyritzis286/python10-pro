"""Simulate rolling a six sided dice"""
import random

DICE_MIN =1
DICE_MAX = 6

def main() -> None:
    """Simulate rolling a six sided dice"""
    for i in range(5):
        dice1 =  random.randint(DICE_MIN, DICE_MAX)
        dice2 =  random.randint(DICE_MIN, DICE_MAX)
        print(f"Roll {i+1}: {dice1}, {dice2}")

if __name__ == "__main__":
    main()