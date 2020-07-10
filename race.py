# Describe WHAT to do = Functional
# functions are a good way to go

# no shared variables (global)
# functions take parameters
# no variables instantiated inside functions

# instead of loops use states called recursively
# All data changes are done with return values

from random import random

def move_cars(car_positions):
    return list(map(lambda x: x + 1 if random() > 0.3 else x, car_positions))

def output_car(car_position):
    return '-' * car_position

def run_step_of_race(state):
    return {'time' : state['time'] - 1,
            'car_positions' : move_cars(state['car_positions'])}

def draw(state):
    print('')
    print('\n'.join(map(output_car,state['car_positions'])))

def show_state(state):
    print('')
    print(state)

def race(state):
    draw(state)
    # show_state(state)
    if (state['time'] > 1):
        race(run_step_of_race(state))

race({'time' : 10, 
      'car_positions' : [1, 1, 1]})

