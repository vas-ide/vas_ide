from datetime import datetime, timedelta


def working_hours(
        date1: str, date2: str, start_time: str, end_time: str, holy: list[str]) -> int | float:
    holy_lst = [datetime.strptime(i, '%Y-%m-%d') for i in holy]
    date1 = datetime.strptime(date1, '%Y-%m-%d')
    date2 = datetime.strptime(date2, '%Y-%m-%d')
    days_lst = []
    day_now = date1
    for _ in range(1000000):
        if day_now in holy_lst:
            day_now += timedelta(days=1)
        elif day_now.weekday() in [5, 6]:
            day_now += timedelta(days=1)
        elif day_now <= date2:
            days_lst.append(day_now)
            day_now += timedelta(days=1)

    print(days_lst)
    time1 = datetime.strptime(start_time, "%H:%M")
    time2 = datetime.strptime(end_time, "%H:%M")
    time_per_day = (time2 - time1).seconds
    total_time = time_per_day * len(days_lst)
    print(time_per_day)
    print(total_time)
    if f"{total_time/3600}"[-1] == "0":
        print(int(total_time/3600))
        return int(total_time/3600)
    else:
        print(round(total_time / 3600, 2))
        return round(total_time / 3600, 2)


#
# working_hours("2023-03-01", "2023-03-01", "09:00", "17:00", [])
# working_hours("2023-03-01", "2023-03-05", "09:00", "17:00", ["2023-03-01"])
# working_hours("2023-03-01", "2023-03-05", "08:45", "17:10", ["2023-03-03"])
working_hours('2023-04-17', '2023-04-30', '08:15', '17:45', ['2023-04-19', '2023-04-21', '2023-04-28'])
# assert working_hours("2023-03-01", "2023-03-01", "09:00", "17:00", []) == 8
# assert working_hours("2023-03-01", "2023-03-02", "09:00", "17:00", []) == 16
# assert working_hours("2023-03-01", "2023-03-03", "09:00", "17:00", ["2023-03-01"]) == 16
# assert (
#     working_hours("2023-03-01", "2023-03-03", "08:45", "17:10", ["2023-03-03"]) == 16.83
# )
# assert working_hours('2023-04-17', '2023-04-30', '08:15', '17:45', ['2023-04-19', '2023-04-21', '2023-04-28']) == 66.5