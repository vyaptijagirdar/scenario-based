
import csv
import re
import argparse


def read_customers(filename):
    customers = []

    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.DictReader(file)

            for row in reader:
                customers.append(row)

    except FileNotFoundError:
        print("Error: CSV file not found!")
        return []

    return customers


def display_customers(customers):
    print("\n----- All Customer Records -----")

    if not customers:
        print("No customer records found.")
        return

    for customer in customers:
        for key, value in customer.items():
            print(f"{key}: {value}")
        print("--------------------------")


def validate_account_number(account_number):
    # Account number must contain exactly 10 digits
    pattern = r'^\d{10}$'

    return re.fullmatch(pattern, account_number) is not None


def search_customer(customers, account_number):
    if not validate_account_number(account_number):
        print("Invalid Account Number!")
        print("Account number must contain exactly 10 digits.")
        return

    print("\n----- Customer Search Result -----")

    found = False

    for customer in customers:
        if customer['Account Number'] == account_number:
            for key, value in customer.items():
                print(f"{key}: {value}")
            found = True
            break

    if not found:
        print("Customer account not found.")


def main():
    parser = argparse.ArgumentParser(
        description="Bank Customer Record System"
    )

    parser.add_argument(
        "filename",
        help="CSV file containing customer records"
    )

    args = parser.parse_args()

    customers = read_customers(args.filename)

    if not customers:
        return

    display_customers(customers)

    account_number = input("\nEnter Account Number to search: ")

    search_customer(customers, account_number)


if __name__ == "__main__":
    main()
