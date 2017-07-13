import future
import os
from random import gauss

from price_feed import *

USER_ID_LENGTH = 30


# configurable distribution of wealth for users (in crypto)
def user_wealth_dist():
    MU = 100
    STD = 30
    return max(0, gauss(MU, STD))


class User(object):
    def __init__(self):
        self.id = os.urandom(USER_ID_LENGTH)
        self.num_tokens = 0
        self.num_crypto = user_wealth_dist() # random wealth


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
    def buy_token_for_crypto(self, user, num_tokens):
        ether_to_usd = self.feed.price

        crypto_cost = ether_to_usd * num_tokens

        # check the user has enough crypto
        if user.num_crypto < crypto_cost:
            return # TODO exception/log

        # TODO is this saved by reference??
        # else let user handle this...
        user.num_crypto -= crypto_cost

        if self.balances[user.id]:
            self.balances[user.id] += num_tokens
        else:
            self.balances[user.id] = num_tokens

        return

    def sell_token_for_crypto(self, user, num_tokens):
        if balances[user.id] < amount_token:
            return # TODO exception/log

        return

if __name__ == '__main__':
    print("Testing bank.py...")
    f = PriceFeed()
    b = Bank(f)
