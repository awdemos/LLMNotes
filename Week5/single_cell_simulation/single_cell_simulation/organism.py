import random

class SingleCellOrganism:
    def __init__(self):
        self.position = [0, 0]
        self.energy = 100
        self.sensors = {
            "chemical": 0,
            "light": 0,
            "temperature": 0,
            "mechanical": 0
        }
    
    def sense_environment(self, environment):
        for sensor in self.sensors:
            self.sensors[sensor] = environment.get_stimulus(sensor, self.position)
    
    def move(self):
        # Implement movement based on sensory input
        dx = random.uniform(-1, 1)
        dy = random.uniform(-1, 1)
        self.position[0] += dx
        self.position[1] += dy
        self.energy -= 1
    
    def interact(self, environment):
        # Implement interactions with the environment
        food = environment.get_food(self.position)
        self.energy += food
