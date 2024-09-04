'''
Funktionerne i kinematics_module er meget generelle.
De kan regne impuls, acceleration og fartændring uanset kontekst.
Dette giver kinematics_module følgende egenskaber:

kinematics_module er meget genbrugelig
kinematics_module er let at teste
kinematics_module er let at forstå/debugge

Funktioner er gode når de er nemme at forstå og fuldkommen adskiller sit
ansvar fra konteksten eller er meget eksplicitte om sin tiltænkte kontekst. '''


def calc_momentum(mass_kg, speed_ms):

    momentum = mass_kg * speed_ms
    return momentum 


def apply_force(target_kg, force_N):

    acceleration = force_N / target_kg
    return acceleration


def apply_acceleration(speed_ms, acceleration_ms2, duration_s):

    delta_v = acceleration_ms2 * duration_s
    speed_ms = speed_ms + delta_v
    return speed_ms


if __name__ == '__main__':
    pass