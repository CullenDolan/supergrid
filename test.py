import datetime
# import calendar


start_date = datetime.datetime(2018,1,1,6)
# how many 5 min blocks needed
hours_per_day = 12
slot_increment = 5
slot_inc_in_datetime = datetime.timedelta(minutes=slot_increment)
slots_per_hour = 60 / slot_increment
slots_per_day = slot_increment * slots_per_hour * hours_per_day
slot = 0
print(start_date)
slot_list = []
while slot < slots_per_day:
    slot_list.append(datetime.datetime.strftime(start_date, '%Y-%m-%d %H:%M'))
    start_date += slot_inc_in_datetime
    slot += slot_increment
print(type(slot_list))