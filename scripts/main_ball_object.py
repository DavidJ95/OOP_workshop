from dropkick import ball_object
import numpy as np


def main(ball_object, drop_duration_s, kick_force_N):
    ''' Script that examines ball behavior when kicked and dropped.
    
    OOP (Object-Orientered Python) has the advantage over using purely functions,
    that objects can have states and attributes that persist for as long as needed.
    States are made up of attributes such as forces acting on other attributes,
    such as momentum. With OOP, the methods in this assignment need less specificity.

    Hint: In an action such as a kick, a force is only applied
    as long as there is contact between the foot and the ball.
    '''

    print(ball_object)
    ball_object.drop(drop_duration_s = drop_duration_s)

    print(ball_object)
    ball_object.kick(force_N = kick_force_N)

    print(ball_object)

    for time_after_kicked_s in np.arange(0.2, 2.2, 0.2):
        ball_object.update_state(duration_s = 0.2)
        print(f" \n Time elapsed: {np.round(time_after_kicked_s,2)} s")
        print(ball_object)

if __name__ == '__main__':

    ball = ball_object.Ball(mass_kg = 2)
    main(ball_object = ball, drop_duration_s = 2, kick_force_N = 1000)