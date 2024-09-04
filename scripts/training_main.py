from src import training_module
from src import training_objects
from src import kinematics_module

import pandas as pd

def main():
    fct_output = training_module.first_function()
    fct_output2 = training_module.second_funtion(fct_output)

    first_joke_in_history = training_objects.JokeObject()
    first_joke_in_history.print_joke()

    return

main()