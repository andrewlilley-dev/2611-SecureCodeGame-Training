'''
Please note:

The first file that you should run in this level is tests.py for database creation.
The attack below is rejected by the symbol validation in code.py and does not change the database.

If you like to return to the initial state of the database, please delete the database (level-4.db) and run 
the tests.py again to recreate it.
'''

import unittest
import code as c

# code.py has 5 methods namely:
# (1) get_stock_info
# (2) get_stock_price
# (3) update_stock_price
# (4) exec_multi_query
# (5) exec_user_script

# The symbol-based methods reject invalid stock symbols. The arbitrary-query methods
# (4) and (5) remain intentionally unsafe for this training exercise.

# Here we show an injection attempt against (2) get_stock_price, which is also rejected
# by methods (1) and (3).

# We believe that methods (4) and (5) shouldn't exist at all in the code.
# Have a look on solution.py for the why.

class TestDatabase(unittest.TestCase):

    # verifies that an injected query is rejected without changing the stock price
    def test_rejects_injected_stock_symbol(self):
        op = c.DB_CRUD_ops()

        price_before = op.get_stock_price('MSFT')
        with self.assertRaisesRegex(ValueError, "Inputted stock symbol is not valid"):
            op.get_stock_price("MSFT'; UPDATE stocks SET price = '525' WHERE symbol = 'MSFT'--")
        self.assertEqual(op.get_stock_price('MSFT'), price_before)

# Further injection attempts should also be rejected:
# "MSFT'; DROP TABLE stocks--"
# through:
# op.get_stock_price("MSFT'; DROP TABLE stocks--")

if __name__ == '__main__':
    unittest.main()