import future
from random import uniform

# assume this is number of crypto per single peg currency
# e.g. 1.2 ether per 1 USD
INITIAL_PRICE = 1
PRICE_DELTA_MULT_FLOOR = 0.9
PRICE_DELTA_MULT_CEIL = 1.1
# assume price is always non-zero because life gets boring thereafter
PRICE_FLOOR = 1e-3

class PriceFeed(object):
    def __init__(self):
        self.price = INITIAL_PRICE
        return

    # return current price _and_ iterate it
    # for read-only use feed.price
    def tick(self):
        current_price = self.price
        self.price = max(PRICE_FLOOR, uniform(PRICE_DELTA_MULT_FLOOR, PRICE_DELTA_MULT_CEIL) * self.price)
        return current_price


if __name__ == '__main__':
    print("Testing price_feed.py...")

    feed = PriceFeed()
    for i in xrange(100):
        print(feed.get())
