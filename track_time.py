from datetime import datetime, timedelta


def get_time_set(date_time_1, date_time_2):
    # start time, end time are divided into 30minutes intervals
    list_ = list()
    base_time = date_time_1
    list_.append(str(base_time))
    while True:
        base_time += timedelta(minutes=30)
        list_.append(str(base_time))
        if base_time >= date_time_2:
            break
    list_.sort()
    return list_


def get_worked_time_pairs(time_sets):
    # creates start time, end time pairs of actual utilization
    set_ = set()
    for i in range(0, len(time_sets) - 1):
        set_.add((time_sets[i], time_sets[i + 1]))
    return set_


def decimal_to_minutes(decimal_number):
    # converts decimal number into hours and minutes
    hours = int(decimal_number)
    minutes = int((decimal_number - hours) * 60)
    return "{} minutes".format(hours * 60 + minutes)


# solution
def emplyee_task_tracker(data):
    date_format = "%Y-%m-%d %H:%M:%S"
    result = set()
    actual_time_allocated = 0
    for start_time, end_time in data:
        date_object_1 = datetime.strptime(start_time, date_format)
        date_object_2 = datetime.strptime(end_time, date_format)
        scheduled_times_difference = date_object_2 - date_object_1
        actual_time_allocated += scheduled_times_difference.total_seconds() / 3600
        time_sets = get_time_set(date_object_1, date_object_2)
        actual_utilization_time_pairs = get_worked_time_pairs(time_sets)
        result |= actual_utilization_time_pairs
    scheduled_allocated_mints = decimal_to_minutes(actual_time_allocated)
    actual_utilization_mints = decimal_to_minutes(len(result) * (1 / 2))
    return "Scheduled Allocated Mints: {} \nActual Utilization Mints: {}".format(
        scheduled_allocated_mints, actual_utilization_mints
    )


if __name__ == "__main__":
    data = (
        ("2023-01-03 11:00:00", "2023-01-03 12:00:00"),
        ("2023-01-03 11:30:00", "2023-01-03 12:30:00"),
        ("2023-01-03 14:00:00", "2023-01-03 16:00:00"),
        ("2023-01-03 15:00:00", "2023-01-03 15:30:00"),
    )
    result = emplyee_task_tracker(data)
    print(result)
    # output:
