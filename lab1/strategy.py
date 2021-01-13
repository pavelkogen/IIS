class Order:
    def __init__(self, price, discount_strategy=None):
        self.price = price
        self.discount_strategy = discount_strategy

    def price_after_discount(self):
        if self.discount_strategy:
            discount = self.discount_strategy(self)
        else:
            discount = 0
        return self.price - discount

    def __repr__(self):
        fmt = "<Price: {}, price after discount: {}>"
        return fmt.format(self.price, self.price_after_discount())


def ten_percent_discount(order):
    return order.price * 0.10


def on_sale_discount(order):
    return order.price * 0.25 + 20


def main():
    """
    >>> Order(100)
    <Стоимость: 100, стоимость со скидкой: 100>
    >>> Order(100, discount_strategy=ten_percent_discount)
    <Стоимость: 100, стоимость со скидкой: 90.0>
    >>> Order(1000, discount_strategy=on_sale_discount)
    <Стоимость: 1000, стоимость со скидкой: 730.0>
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
