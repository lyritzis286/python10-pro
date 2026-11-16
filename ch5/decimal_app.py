from decimal import Decimal
from decimal import ROUND_HALF_UP

def main() -> None:
    #orismos tis akriveias ton dekadikon

    #dimiourgia dekadikon arithmon
    price = Decimal("19.99")
    tax_rate = Decimal("0.24")

    vat = price * tax_rate
    total_price = price + vat

    #strogilopiisi tou telikou posou
    total_price = total_price.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    print(total_price)


if __name__ == "__main__":
    main()
