# Ice Cream Simulation Project README

This README file provides detailed information about the Ice Cream Simulation project, which includes the core files `freezer.py`, `ice_cream.py`, and their usage in simulation scripts such as `ice_cream_dream.py`, `test_ice_cream.py`, and `simple_test.py`. These components are designed to help users understand object-oriented programming, specifically class inheritance and unit testing in Python.

## Table of Contents

- [Introduction](#introduction)
- [Setup](#setup)
- [Project Structure](#project-structure)
- [Running Simulations and Tests](#running-simulations-and-tests)
- [Understanding the Code](#understanding-the-code)
- [License](#license)

## Introduction

The project aims to teach users about class inheritance and the basics of unit testing by simulating an ice cream storage system. Users can explore how ice creams of different flavors are managed and stored within a freezer, observing how their states change over time based on environmental interactions.

## Setup

To run this project, clone it from GitHub and navigate to the directory:

```bash
git clone https://github.com/tsmith4014/Class-Inheritance-guide.git
cd Class-Inheritance-guide
```

## Project Structure
Freezer
from ice_cream import IceCream
from ice_cream import FlavoredIceCream
The project contains several key files:

- `freezer.py`: Defines the `Freezer` class that manages collections of ice creams.
- `ice_cream.py`: Includes the `IceCream` base class and the `FlavoredIceCream` subclass.
- `ice_cream_dream.py`: Utilizes the `Freezer`, `IceCream`, and `FlavoredIceCream` classes to simulate a full ice cream management system.
- `test_ice_cream.py`: Contains unit tests for the ice cream classes and their interactions within the freezer.  This is a unittest and may require a pip install.
- `simple_test.py`: (Start here) Demonstrates basic functionalities of the classes in a simplified manner.

## Running Simulations and Tests

### Simulations

### Unit Testing

To ensure that all components work as expected, run the unit tests:

```bash
python -m unittest test_ice_cream.py
```

This command runs the tests defined in `test_ice_cream.py`, covering various functionalities of the ice creams and freezer.

### Simple Test Script

For a quick demonstration of basic class functionality without running the full simulation:

```bash
python simple_test_here.py
```

## Understanding the Code

The core idea is to show how `IceCream` and `FlavoredIceCream` classes inherit properties and methods, and how they interact within the `Freezer`. Testing these interactions helps validate that the system behaves as expected under different conditions.

## License

This project is provided under the MIT License. See the LICENSE file in the GitHub repository for full details.
