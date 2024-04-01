# mountain-climber

The Mountain Trail Manager is a Python program that allows users to manage and interact with a network of mountain trails. It provides functionality to add mountains, remove mountains, query mountains, load and save trail data, simulate a walker's path, organize mountains, and display mountain positions.

## Features

- Add new mountains to the trail network
- Remove existing mountains from the trail network
- Query the list of mountains in the trail network
- Load trail data from a file
- Save trail data to a file
- Simulate a walker's path through the trail network based on different personalities
- Organize mountains based on their difficulty and name
- Display the positions of the mountains after organization

## Requirements

- Python 3.x
- `sortedcontainers` library (can be installed using `pip install sortedcontainers`)

## Installation

1. Clone the repository:
>>>git clone https://github.com/joshbatties/mountain-climber.git

2. Navigate to the project directory:
>>>cd mountain-trail-manager

3. Install the required dependencies:
>>>pip install sortedcontainers

## Usage

1. Run the program:
>>>python main.py

2. The program will display a menu with different options:
- Add Mountain
- Remove Mountain
- Query Mountains
- Load Trail Data
- Save Trail Data
- Simulate Walker's Path
- Organize Mountains
- Display Mountain Positions
- Quit

3. Enter the corresponding number to perform a specific action.

4. Follow the prompts to provide the necessary information for each action.

5. The program will execute the selected action and display the results.

6. To quit the program, choose option `9` from the menu.

## File Structure

- `main.py`: The main entry point of the program.
- `cli.py`: Implements the command-line interface for interacting with the program.
- `mountain.py`: Defines the `Mountain` class representing a mountain.
- `mountain_manager.py`: Implements the `MountainManager` class for managing a collection of mountains.
- `trail.py`: Defines the `Trail` class and related classes for representing a trail network.
- `mountain_organiser.py`: Implements the `MountainOrganiser` class for organizing mountains based on difficulty and name.
- `personality.py`: Defines different walker personalities for simulating a walker's path through the trail network.
- `serialize.py`: Provides functions for serializing and deserializing trail data.