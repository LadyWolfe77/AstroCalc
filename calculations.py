# The actual astronomy equations.

# Distance, speed, and time calculations.

def calculate_distance(speed, time):
    return speed * time


def calculate_speed(distance, time):
    return distance / time


def calculate_time(distance, speed):
    return distance / speed


# Solar System scale calculation.

def calculate_scaled_distance(distance_km, strip_length_cm):
    pluto_distance = 5.91e9
    scale_factor = strip_length_cm / pluto_distance

    return distance_km * scale_factor