import unittest
import datetime
from end_of_budget_based_on_burn_rate import workdayadd, workdaysub


(MON, TUE, WED, THU, FRI, SAT, SUN) = range(7)

class TestEndOfBudgetBasedOnBurnRate(unittest.TestCase):

	def testworkdayadd(self):
		workdays = workdayadd(datetime.datetime(2015,1,1), 10, whichdays=(MON,TUE,WED,THU,FRI))
		self.assertEqual(workdays, datetime.datetime(2015,1,15))

	def testworkdaysub(self):
		workdays = workdaysub(datetime.datetime(2015,1,1),datetime.datetime(2015,1,2))
		self.assertEqual(workdays, 2)

if __name__ == '__main__':
    unittest.main()