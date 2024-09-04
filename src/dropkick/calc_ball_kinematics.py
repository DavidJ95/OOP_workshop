import kinematics_module


def drop_a_ball(ball_mass_kg, duration_s):
    ''' 
    Returnerer ny hastighed, impuls og acceleration efter at være
    tabt og falde i en antal sekunder. 
    '''

    ball_acceleration = -9.82
    print(" \n Dropping ball...")
    ball_new_speed_ms = kinematics_module.apply_acceleration(speed_ms = 0, acceleration_ms2 = ball_acceleration, duration_s = duration_s)
    ball_new_momentum = kinematics_module.calc_momentum(ball_mass_kg, ball_new_speed_ms)

    return ball_new_speed_ms, ball_new_momentum, ball_acceleration


def kick_a_ball(ball_mass_kg, ball_init_speed_ms, force_N):
    '''
    Returnerer ny hastighed og impuls efter at blive sparket til.
    Funktionen antager at sparket er den eneste kraft der påvirker bolden.
    '''
    
    ball_init_momentum = kinematics_module.calc_momentum(ball_mass_kg, ball_init_speed_ms)
    print(f' \n Before kick, ball has momentum of {ball_init_momentum} kg m/s')

    print(" \n Kicking ball...")
    ball_acceleration = kinematics_module.apply_force(ball_mass_kg, force_N)
    ball_new_speed_ms = kinematics_module.apply_acceleration(speed_ms = ball_init_speed_ms, acceleration_ms2 = ball_acceleration, duration_s = 0.08)

    ball_new_momentum = kinematics_module.calc_momentum(ball_mass_kg, ball_new_speed_ms)

    return ball_new_speed_ms, ball_new_momentum