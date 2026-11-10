'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
from decimal import Decimal

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')
OrderMax = 100
OrderMin = 0
ItemMax = 100000
PaymentMax = 1e6

def validorder(order: Order):
    payments = Decimal(0)
    expenses = Decimal(0)

    for item in order.items:
        if item.type == 'payment':
            if  -ItemMax <= item.amount <= ItemMax:
                payments += Decimal(str(item.amount))
        elif item.type == 'product':
            if type(item.quantity) is int and OrderMin < item.quantity <= OrderMax and OrderMin < item.amount <= ItemMax:
                expenses += Decimal(str(item.amount)) * Decimal(str(item.quantity))
        else:
            return "Invalid item type: %s" % item.type

    if abs(payments) > PaymentMax or expenses > PaymentMax:
        return "Total amount payable for an order exceeded"

    if payments != expenses:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, payments - expenses)
    else:
        return "Order ID: %s - Full payment received!" % order.id