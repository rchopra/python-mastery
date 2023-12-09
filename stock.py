"""stock.py"""


class Stock:
    """The stock class."""

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        """Calculate cost."""
        return self.shares * self.price
