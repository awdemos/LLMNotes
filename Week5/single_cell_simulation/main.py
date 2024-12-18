from single_cell_simulation.simulation import run_simulation
import matplotlib.pyplot as plt

def main():
    positions, energies = run_simulation(1000)
    
    # Visualize the results
    plt.figure(figsize=(12, 5))
    plt.subplot(121)
    plt.plot([p[0] for p in positions], [p[1] for p in positions])
    plt.title("Organism Path")
    plt.subplot(122)
    plt.plot(energies)
    plt.title("Organism Energy")
    plt.show()

if __name__ == "__main__":
    main()

