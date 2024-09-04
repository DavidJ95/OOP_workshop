from src import module
from src import objects
from src import kinematics_module

import pandas as pd

def main():
    fct_output = module.first_function()
    fct_output2 = module.second_funtion(fct_output)

    first_joke_in_history = objects.JokeObject()
    first_joke_in_history.print_joke()

    return

main()