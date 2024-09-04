from dropkick import calc_ball_kinematics
from src import kinematics_module

import numpy as np


def main(ball_mass_kg, ball_init_speed_ms, kick_force_N, drop_duration_s):
    ''' Regner på en bolds impuls før og efter den bliver sluppet og sparket til. 

        main-programmet skal håndtere mange parametre: 
            Kræver læselighed og gode variabelnavne!
            Ser stadig rodet ud bagefter
        '''

    print(f' \n\n Ball has mass {ball_mass_kg} kg, speed {ball_init_speed_ms} m/s')
    ball_speed_ms, ball_momentum, ball_acceleration = calc_ball_kinematics.drop_a_ball(ball_mass_kg, drop_duration_s)
    
    print(f' \n After dropping for {drop_duration_s} s, ball has a new speed of {ball_speed_ms} m/s and momentum of {ball_momentum} kg m/s')

    ball_speed_ms, ball_momentum = _kick_an_accelerating_ball(
        ball_mass_kg, ball_speed_ms, kick_force_N, ball_acceleration)
    
    print(f' \n After kick, ball now has a new speed of {np.round(ball_speed_ms,2)} m/s and momentum of {np.round(ball_momentum,2)} kg m/s')

    for time_after_kicked_s in np.arange(0.2, 2.2, 0.2):
        ball_speed_ms = kinematics_module.apply_acceleration(speed_ms = ball_speed_ms, acceleration_ms2 = -9.82, duration_s = 0.2)
        print(f" \n Time elapsed: {np.round(time_after_kicked_s,2)} s")
        print(f"New speed: {np.round(ball_speed_ms, 2)}, new momentum: {np.round(ball_mass_kg * ball_speed_ms, 2)}")


def _kick_an_accelerating_ball(ball_mass_kg, ball_init_speed_ms, force_N, ball_acceleration):
    ''' 
    En funktton der er specifik nok til at vi putter den ind i vores main-script.
    Funktionen antager at bolden allerede har en acceleration og kalder
    sparkefunktionen med nettokraften på bolden. '''

    init_force_N = ball_mass_kg * ball_acceleration
    kick_force_N = init_force_N + force_N

    return calc_ball_kinematics.kick_a_ball(ball_mass_kg, ball_init_speed_ms, kick_force_N)


if __name__ == '__main__':
    main(ball_mass_kg = 2, ball_init_speed_ms = 0, drop_duration_s = 2, kick_force_N = 1000)