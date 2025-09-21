def exchange_money(budget, exchange_rate):
    """
    formula
    """
    return budget / exchange_rate
 

    


def get_change(budget, exchanging_value):
    """
    formula
    """
    return budget - exchanging_value
  

  


def get_value_of_bills(denomination, number_of_bills):
    """
    formula
    """
    return denomination * number_of_bills

    


def get_number_of_bills(amount, denomination):
    """
    formula
    """
    return amount // denomination


    


def get_leftover_of_bills(amount, denomination):
    """
    formula
    """
    return amount % denomination 
    

    


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    formula 
    """
    return int((budget/(exchange_rate*(1+spread/100)))//denomination*denomination)
    

    
