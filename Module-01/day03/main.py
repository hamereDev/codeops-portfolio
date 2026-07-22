def read_transactions(filename):
    customer_totals = {}

    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                customer, amount = line.split(",")
                amount = float(amount)

                if customer in customer_totals:
                    customer_totals[customer] += amount
                else:
                    customer_totals[customer] = amount

    except FileNotFoundError:
        print(f"Error: '{filename}' was not found.")
        return {}

    return customer_totals


def create_summary_report(customer_totals, output_file):
    sorted_customers = sorted(
        customer_totals.items(),
        key=lambda item: item[1],
        reverse=True
    )

    with open(output_file, "w") as report:
        report.write("Telebirr Customer Spending Report\n")

        for customer, total in sorted_customers:
            line = f"{customer}: {total:.2f} ETB"
            print(line)
            report.write(line + "\n")


def main():
    transactions = read_transactions("telebirr_transactions.txt")

    if transactions:
        create_summary_report(
            transactions,
            "summary_report.txt"
        )


if __name__ == "__main__":
    main()