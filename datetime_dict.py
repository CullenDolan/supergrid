import get_slots
def printing_func():
    print(type(slots))
    print(slots)

"""from datetime import datetime

new_dict = {datetime(2021,2,9,6):123, datetime(2021,2,9,6,5):0, datetime(2021,2,9,6,10):456}

print(new_dict)

ask_year = int(input('Year: '))
ask_month = int(input('Month: '))
ask_day = int(input('Day: '))
ask_hour = int(input('Hour: '))
ask_min = int(input('Min: '))
ask_provider_id = int(input('Provider ID: '))

if new_dict[datetime(ask_year, ask_month, ask_day, ask_hour, ask_min)] == 0:
    new_dict[datetime(ask_year, ask_month, ask_day, ask_hour, ask_min)]=ask_provider_id
else:
    print('That time slot is taken by ' + str(new_dict[datetime(ask_year, ask_month, ask_day, ask_hour, ask_min)]))

print(new_dict)"""

if __name__ == "__main":
    printing_func()
    get_slots.get_time_slots()