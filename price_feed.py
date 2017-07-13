import future
from random import uniform

# assume this is number of crypto per single peg currency
# e.g. 1.2 ether per 1 USD
INITIAL_PRICE = 1
PRICE_DELTA_MULT_FLOOR = 0.9
PRICE_DELTA_MULT_CEIL = 1.1

class PriceFeed(object):
    def __init__(self):
        self.price = INITIAL_PRICE
        return

    # return a random number
    def get(self):
        current_price = self.price
        self.price = uniform(PRICE_DELTA_MULT_FLOOR, PRICE_DELTA_MULT_CEIL) * self.price
        return current_price


if __name__ == '__main__':
    print("Testing price_feed.py...")

    feed = PriceFeed()
    for i in xrange(100):
        print(feed.get())
