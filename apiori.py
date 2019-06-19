import numpy as np
from itertools import combinations, groupby
from collections import Counter
import pandas as pd
import sys
from itertools import combinations, groupby
from collections import Counter
from IPython.display import display

# Sample data
orders = np.array([[1, 'apple'], [1, 'egg'], [1, 'milk'], [2, 'egg'], [2, 'milk']], dtype=object)


# Generator that yields item pairs, one at a time
def get_item_pairs(order_item):
    # For each order, generate a list of items in that order
    for order_id, order_object in groupby(orders, lambda x: x[0]):
        item_list = [item[1] for item in order_object]

        # For each item list, generate item pairs, one at a time
        for item_pair in combinations(item_list, 2):
            yield item_pair

        # Counter iterates through the item pairs returned by our generator and keeps a tally of their occurrence


Counter(get_item_pairs(orders))
print(Counter(get_item_pairs(orders)))

# Function that returns the size of an object in MB
def size(obj):
    return "{0:.2f} MB".format(sys.getsizeof(obj) / (1000 * 1000))
orders = pd.read_csv('D:\\study\\fourth academic year\\firstTerm\\KBS\\project\\datamining\\Data.csv')
print('orders -- dimensions: {0};   size: {1}'.format(orders.shape, size(orders)))
display(orders.head())