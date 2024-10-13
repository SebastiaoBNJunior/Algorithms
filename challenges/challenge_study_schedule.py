def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    students = 0
    if not target_time:
        return None
    for period in permanence_period:
        if type(period[0]) is not int or type(period[1]) is not int:
            return None
        if period[0] <= target_time <= period[1]:
            students += 1

    return students
