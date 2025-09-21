"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active, touching_ghost):
    return power_pellet_active and touching_ghost == True

def score(touching_power_pellet, touching_dot):
    return touching_power_pellet or touching_dot == True

def lose(power_pellet_active, touching_ghost):
    
    return touching_ghost and not power_pellet_active
   


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    return has_eaten_all_dots and not power_pellet_active and not touching_ghost == True or has_eaten_all_dots and power_pellet_active and touching_ghost == True
