# load library
import datetime

# find number of days between two dates
today = datetime.date.today()

someday = datetime.date(2016, 11, 11)

diff = someday - today

print ('days: ' + str(diff.days))
# -655
