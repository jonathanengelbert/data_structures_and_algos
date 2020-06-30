number_of_steps = 10
steps = 'DUDDDUUDUU'

def valley_counter(n, s):
    valley_count = 0
    altitude = 0
    in_valley = False

    for step in s:
        if step == 'U':
            altitude += 1
        if step == 'D':
            altitude -= 1

        if altitude <= -1 and not in_valley:
            in_valley = True
        if altitude is 0 and in_valley:
            in_valley = False
            valley_count += 1

    return valley_count


print(valley_counter(number_of_steps, steps))