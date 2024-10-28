# Ruckus

Ruckus is a Rubik's Cube solving bot powered by a microcontroller and six NEMA 17 stepper motors. The bot automates the process of solving a Rubik's Cube by performing calculated rotations to reach the solved state. This project requires the SimpleSerial Python library for serial communication between the Python control script and the microcontroller.


# Requirements

### Hardware
-   Microcontroller (compatible with SimpleSerial communication)
-   6 x NEMA 17 Stepper Motors
-   Rubik's Cube fixture for secure mounting and movement of the cube

### Software
-   Python 3.12 or higher
-   SimpleSerial Python library

## Installation

1.  **Clone this repository**:
git clone https://github.com/Mekyle-Hemani/ruckus.git 

2.  **Install SimpleSerial**:
pip install SimpleSerial

3.  **Upload /arduino/Ruckus/src/main.cpp to microcontroller**


## Usage

1.  **Run the Main Script**:

    `python main.py`


## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any bugs or feature requests.
