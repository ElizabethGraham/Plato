import pygame
import time
import emotions_scratch


class Plato(object):
    def __init__(self, name, age, is_alive, is_awake):
        self.stats = {"happiness": 100, "power": 100}
        self.name = 'Plato'
        self.age = age
        self.is_alive = True
        self.is_awake = True
        self.name = name
    def check_age(self):
        # Write birthday to file
        # Check birthday
        # Check current day
        # Determine age from birthday / current day
        pass
    def check_is_alive(self):
        if not self.is_alive:
            # Kill Plato
            # Write death details to file
            pass
    def check_is_awake(self):
        if not self.is_awake:
            # If is_awake = false, run sleep functions
            pass
