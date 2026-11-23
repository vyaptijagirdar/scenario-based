
import csv
import argparse

def read_mobiles(filename):
    mobiles = []

    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.DictReader(file)

            for row in reader:
                mobiles.append(row)

    except FileNotFoundError:
        print("Error: CSV file not found!")
        return []

    return mobiles


def display_mobiles(mobiles):
    print("\n----- All Mobile Records -----")

    if not mobiles:
        print("No mobile records found.")
        return

    for mobile in mobiles:
        for key, value in mobile.items():
            print(f"{key}: {value}")
        print("------------------------")


def search_mobile(mobiles, brand):
    print("\n----- Search Results -----")

    found = False

    for mobile in mobiles:
        if mobile['Brand Name'].lower() == brand.lower():
            for key, value in mobile.items():
                print(f"{key}: {value}")
            print("------------------------")
            found = True

    if not found:
        print("Mobile brand not found.")


def main():
    parser = argparse.ArgumentParser(
        description="Mobile Store Record System"
    )

    parser.add_argument(
        "filename",
        help="CSV file containing mobile records"
    )

    args = parser.parse_args()

    mobiles = read_mobiles(args.filename)

    if not mobiles:
        return

    display_mobiles(mobiles)

    brand = input("\nEnter Brand Name to search: ")
    search_mobile(mobiles, brand)


if __name__ == "__main__":
    main()
