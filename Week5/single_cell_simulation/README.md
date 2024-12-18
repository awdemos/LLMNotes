# Single Cell Organism Simulation

A Python-based simulation that models the behavior of a single-celled organism moving through its environment while managing energy resources.

## Overview

This project simulates a simple single-celled organism's movement and energy dynamics in a 2D environment. The organism:
- Navigates through a randomized environment
- Senses various environmental stimuli (chemical, light, temperature, mechanical)
- Gathers and manages energy resources
- Demonstrates emergent behavior patterns

## Features

- **Environmental Sensing**: Multiple sensor types for detecting various stimuli
- **Energy Management**: Dynamic energy consumption and acquisition
- **Movement Patterns**: Random walk with environmental influence
- **Real-time Visualization**: 
  - Movement trajectory plotting
  - Energy level monitoring
- **Customizable Parameters**: Adjustable simulation parameters

## Installation

1. Ensure you have Poetry installed:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. Clone the repository:
```bash
git clone [repository-url]
cd single-cell-simulation
```

3. Install dependencies using Poetry:
```bash
poetry install
```

## Usage

Run the simulation using Poetry:
```bash
poetry run simulate
```

The simulation will display two plots:
- Left: Organism's movement path
- Right: Energy levels over time

## Project Structure

```
single_cell_simulation/
├── pyproject.toml
├── README.md
├── main.py
├── single_cell_simulation/
│   ├── __init__.py
│   ├── organism.py      # Organism behavior definition
│   ├── environment.py   # Environment parameters
│   └── simulation.py    # Core simulation logic
└── tests/
    └── __init__.py
```

## Technical Details

### Components

- **Organism**: 
  - Maintains position and energy levels
  - Contains sensory mechanisms
  - Implements movement logic

- **Environment**:
  - Generates chemical gradients
  - Creates light and temperature maps
  - Manages food distribution

- **Simulation**:
  - Coordinates organism-environment interactions
  - Tracks movement and energy data
  - Handles visualization

### Dependencies

- Python 3.12+
- NumPy: Environmental calculations
- Matplotlib: Visualization
- Poetry: Package management

## Results

The simulation produces:
1. A movement trajectory showing the organism's path through space
2. An energy graph displaying the organism's energy levels over time

## Contributing

Contributions are welcome! Some areas for potential enhancement:
- Advanced movement algorithms
- More complex environmental factors
- Additional visualization options
- Performance optimizations

## License

MIT License - See LICENSE file for details

Citations:
[1] https://pplx-res.cloudinary.com/image/upload/v1734548483/user_uploads/xOlxYdfLZlqyetu/image.jpg
