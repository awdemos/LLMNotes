from .organism import SingleCellOrganism
from .environment import Environment

def run_simulation(num_steps):
    environment = Environment(100)
    organism = SingleCellOrganism()
    
    positions = []
    energies = []
    
    for _ in range(num_steps):
        organism.sense_environment(environment)
        organism.move()
        organism.interact(environment)
        
        positions.append(organism.position.copy())
        energies.append(organism.energy)
    
    return positions, energies

