import future
import os

from price_feed import *

USER_ID_LENGTH = 30

class User(object):
    def __init__(self):
        self.id = os.urandom(USER_ID_LENGTH)


# the bank will always buy 1 token for 1 usd worth of
# crypto (based on a price feed)
class Bank(object):
    def __init__(self, feed):
        self.feed = feed
        self.balances = {}
        self.supply_token = 0
        self.supply_crypto = 0
        return

    # user buys crypto for
    def buy_token_for_crypto(self, user):
        return

    def sell_token_for_crypto(self, user):
        return

if __name__ == '__main__':
    print("Testing bank.py...")
    f = PriceFeed()
    b = Bank(f)
