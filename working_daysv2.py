# Given the current burn rate when will I finish the estimated work?

from datetime import date, timedelta
from datetime import *
from decimal import Decimal
from math import floor

(MON, TUE, WED, THU, FRI, SAT, SUN) = range(7)
today = datetime.now()


def workdaysub(start_date, end_date, whichdays=(MON,TUE,WED,THU,FRI)):
    '''
    Calculate the number of working days between two dates inclusive
    (start_date <= end_date).

    The actual working days can be set with the optional whichdays
parameter
    (default is MON-FRI)
    '''
    delta_days = (end_date - start_date).days + 1
    full_weeks, extra_days = divmod(delta_days, 7)
    # num_workdays = how many days/week you work * total # of weeks
    num_workdays = (full_weeks + 1) * len(whichdays)
    # subtract out any working days that fall in the 'shortened week'
    for d in range(1, 8 - extra_days):
                if (end_date + timedelta(d)).weekday() in whichdays:
                                num_workdays -= 1
    return num_workdays

def workdayadd(start_date,work_days, whichdays=(MON,TUE,WED,THU,FRI)):
    '''
    Adds to a given date a number of working days 
    2009/12/04 for example is a friday - adding one weekday
    will return 2209/12/07
    >>> workdayadd(date(year=2009,month=12,day=4),1) 
    datetime.date(2009, 12, 7)
    '''
    weeks, days = divmod(work_days,len(whichdays))
    new_date = start_date + timedelta(weeks=weeks)
    for i in range(days):
        while new_date.weekday() not in whichdays:
            new_date += timedelta(days=1)
    return new_date

def main():
	spent_to_date = input("What is spent to date (excl PM)? ")
	start_date_input = input("What is the start date? ")
	end_date = today
	dev_days_remaining = input("How many dev work days remaining? ")

	start_date = datetime(*start_date_input[:4])
	num_days = workdaysub(start_date, end_date)
	burn_rate = spent_to_date/num_days
	
	print "Burn Rate: %s " % burn_rate
	
	num_days_at_given_burn = dev_days_remaining/burn_rate

	print "Number of work days required: %s " % num_days_at_given_burn

	expected_end_date = workdayadd(today, int(num_days_at_given_burn))

	print "Expected end date: %s" % expected_end_date

	pass

if __name__ == '__main__':
	main()