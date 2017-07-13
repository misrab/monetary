import future

from price_feed import *
from bank import *



if __name__ == '__main__':
    print("Running main...")

    feed = PriceFeed()
    bank = Bank(feed)
    users = [ User() for i in xrange(10) ]
