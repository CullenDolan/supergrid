from datetime import datetime, timedelta, date


def main():
    # define all the varibles (what probably gets passed in)
    year_start, month_start, day_start = 2018, 1, 1
    hour_start, minute_start = 6, 0
    year_end, month_end, day_end = 2018, 1, 2
    hour_end, minute_end = 18, 0
    work_hours_per_day = 12
    slot_duration_int = 5

    # define the dates and datetimes
    start_datetime = datetime(year_start, month_start, day_start, hour_start, minute_start)
    start_date = date(year_start, month_start, day_start)
    end_datetime = datetime(year_end, month_end, day_end, hour_end, minute_end)
    end_date = date(year_end, month_end, day_end)
    
    
    slots_per_day = define_slots(work_hours_per_day, slot_duration_int)
    slot_list = return_slot_list(start_datetime, end_datetime, slot_duration_int, slots_per_day)
    print(slot_list)


def return_slot_list(start_datetime, end_datetime, slot_duration_int, slots_per_day):
    # return the list of slots per day
    slot_list = []
    
    while start_datetime <= end_datetime:
        slot = 0
        while slot < slots_per_day:
            slot_list.append(datetime.strftime(start_datetime, '%Y-%m-%d %H:%M'))
            slot += 1
            start_datetime += timedelta(minutes=slot_duration_int)
        start_datetime = start_datetime + timedelta(hours=12)
    return slot_list


def days_on_schedule(start_date, end_date,delta):
    curr = start_date
    while curr <= end_date:
        yield curr
        curr += delta 

def define_slots(work_hours_per_day, slot_duration_int):
    # slots per hour * number of working hours
    mins_in_hr = 60
    slots_per_day =  mins_in_hr / slot_duration_int * work_hours_per_day
    return slots_per_day


if __name__ == '__main__':
    main()