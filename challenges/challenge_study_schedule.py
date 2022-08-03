def study_schedule(permanence_period, target_time):
    time_counter = 0
    for login_time, logout_time in permanence_period:
        try:
            if login_time <= target_time <= logout_time:
                time_counter += 1
        except TypeError:
            return None
    return time_counter
