import numpy as np
import random

class Environment:
    def __init__(self, size):
        self.size = size
        self.chemical_gradient = np.random.rand(size, size)
        self.light_map = np.random.rand(size, size)
        self.temperature_map = np.random.rand(size, size)
        self.food_map = np.random.rand(size, size)
    
    def get_stimulus(self, sensor_type, position):
        x, y = int(position[0]), int(position[1])
        if sensor_type == "chemical":
            return self.chemical_gradient[x, y]
        elif sensor_type == "light":
            return self.light_map[x, y]
        elif sensor_type == "temperature":
            return self.temperature_map[x, y]
        elif sensor_type == "mechanical":
            return random.random()  # Simplified mechanical stimulus
    
    def get_food(self, position):
        x, y = int(position[0]), int(position[1])
        food = self.food_map[x, y]
        self.food_map[x, y] = 0  # Consume the food
        return food * 10  # Convert food to energy
