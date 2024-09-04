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
        return f"\n Acceleration: {np.round(self.acceleration,2)} m/s^2, Speed: {np.round(self.speed,2)} m/s, \n Mass: {np.round(self.mass,2)} kg, Force: {np.round(self.force,2)} N, Momentum: {np.round(self.momentum,2)} kg m/s."

    def _update_momentum(self, duration_s):
        self.momentum = self.momentum + self.force * duration_s

    def _update_speed(self, duration_s):
        self.speed = self.speed + self.acceleration * duration_s
    
    def update_state(self, duration_s):
        self._update_momentum(duration_s)
        self._update_speed(duration_s)

    def apply_force(self, force_N, duration_s = None):
        self.force += force_N
        self.acceleration = self.force / self.mass

        if duration_s is not None:
            self.update_state(duration_s = duration_s)

    def apply_gravity(self, duration_s = None):
        force_N = MassObject.g * self.mass
        self.apply_force(force_N = force_N, duration_s = duration_s) 

    def null_force(self):
        self.force = 0
        self.acceleration = 0