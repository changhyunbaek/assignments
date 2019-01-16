# import datetime

# raw_date = "2017-01-11"
# date_format = "%Y-%m-%d"

# parsed_date = datetime.datetime.strptime(raw_date, date_format)

# print(raw_date)
# print(parsed_date)

# new_pattern = "%m/%d/%y"
# date_str = parsed_date.strftime(new_pattern) # 01/11/17
# print(date_str)


# --------------------------------------------------------------------------------

# Goal: print date as like "5/1/2012".

import datetime


birthday = "1-May-12"

date_format = "%d-%B-%y"
parsed_date = datetime.datetime.strptime(birthday, date_format)

new_pattern = "%-m/%-d/%Y"
parsed_date = parsed_date.strftime(new_pattern)

print(parsed_date)


# --------------------------------------------------------------------------------
