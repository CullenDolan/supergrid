from datetime import datetime, date

# define all the varibles (what probably gets passed in)
year_start = 2018
month_start = 1
day_start = 1
hour_start = 6
minute_start = 0
year_end = 2018
month_end = 1
day_end = 2
hour_end = 18
minute_end = 0
hours_per_day = 12
slot_increment = 5
slot = 0


def main():
    start_date = create_date_time(year_start, month_start, day_start, hour_start, minute_start)
    end_date = create_date_time(year_end, month_end, day_end, hour_end, minute_end)
    slots_per_day,slot_inc_in_datetime = define_slots(hours_per_day, slot_increment)
    #for days in 
    slot_list = return_slot_list(start_date, slot_inc_in_datetime,slot_increment, slot, slots_per_day)
    print(slot_list)


def return_day_list(start_date, end_date):


def return_slot_list(start_date, slot_inc_in_datetime,slot_increment, slot, slots_per_day):
    # return the list of slots per day
    slot_list = []
    while slot < slots_per_day:
        slot_list.append(datetime.strftime(start_date, '%Y-%m-%d %H:%M'))
        start_date += slot_inc_in_datetime
        slot += slot_increment
    return slot_list


def create_date_time(year_inpt,month_inpt,day_inpt,hour_inpt,minute_inpt):
    # define the variables when to start the calendar
    return datetime(year_start, month_start, day_start, hour_start, minute_start)


def define_slots(hours_per_day, slot_increment):
    # define the slot size
    slot_inc_in_datetime = timedelta(minutes=slot_increment)
    slots_per_hour = 60 / slot_increment
    slots_per_day =  slot_increment * slots_per_hour * hours_per_day
    return slots_per_day, slot_inc_in_datetime


if __name__ == '__main__':
    main()