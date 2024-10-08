import numpy as np

class MassObject:

    g = -9.82

    def __init__(self, mass_kg, speed_ms = 0, acceleration_ms2 = 0):
        ''' Enheder ligger i variabelnavne, så vi kan antage SI-enheder herfra '''

        self.mass = mass_kg
        self.speed = speed_ms
        self.acceleration = acceleration_ms2
        self.force = self.mass * self.acceleration
        self.momentum = self.mass * self.speed

    def __str__(self):
        return f"""\n Acceleration: {np.round(self.acceleration,2)} m/s^2, 
        Speed: {np.round(self.speed,2)} m/s, \n 
        Mass: {np.round(self.mass,2)} kg, 
        Force: {np.round(self.force,2)} N, 
        Momentum: {np.round(self.momentum,2)} kg m/s."""
    
    def update_state(self, duration_s):
        self._update_momentum(duration_s)
        self._update_speed(duration_s)

    def apply_force(self, force_N):
        self.force += force_N
        self.acceleration = self.force / self.mass

    def apply_gravity(self):
        force_N = MassObject.g * self.mass
        self.apply_force(force_N = force_N) 