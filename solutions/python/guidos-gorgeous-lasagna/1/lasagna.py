EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2
def bake_time_remaining(elapsed_bake_time):
    '''returns remaining time by extracting from expected time the time lasagna already was in oven '''
    return EXPECTED_BAKE_TIME - elapsed_bake_time
def preparation_time_in_minutes(number_of_layers):
    '''returns preparation time by multipling number of layers with their average preparation time '''
    return number_of_layers * PREPARATION_TIME
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    '''returns elipsed time by taking preparation time and summing it with the time lasagna already in the oven'''
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    