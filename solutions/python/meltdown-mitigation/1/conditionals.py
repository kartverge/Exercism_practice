
def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """
    if temperature < 800 and neutrons_emitted > 500 and temperature*neutrons_emitted<500000:
        return True
    else:
        return False
    


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param theoretical_max_power: int or float - power that corresponds to a 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """
    generated_power = voltage * current
    if (generated_power/theoretical_max_power)*100 >= 80:
        return 'green'
    elif (generated_power/theoretical_max_power)*100 < 80 and(generated_power/theoretical_max_power)*100 >= 60:
        return 'orange'
    elif (generated_power/theoretical_max_power)*100 < 60 and(generated_power/theoretical_max_power)*100 >= 30: 
        return 'red'
    elif (generated_power/theoretical_max_power)*100 < 30:
        return 'black'


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    criticality = temperature * neutrons_produced_per_second # O(n)
    if threshold*0.9 <= criticality <= threshold*1.1:  # O(n) + O(1) + O(n)
        return 'NORMAL'
    if criticality < threshold*0.9:  # O(n) + O(1)
        return 'LOW'
    return 'DANGER'
   
    