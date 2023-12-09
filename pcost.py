"""pcost.py"""


def portfolio_cost(filename):
    """Calcuclate portfolio cost."""
    total = 0.0
    with open(filename, "rb") as f:
        for line in f.readlines():
            _, shares, price = line.split()
            try:
                total += int(shares) * float(price)
            except ValueError as e:
                print("Couldn't parse:", line)
                print("Reason:", e)

    return total


if __name__ == "__main__":
    print(portfolio_cost("Data/portfolio.dat"))
