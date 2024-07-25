# Snake Game

## Overview

This is a simple implementation of the classic Snake game using Pygame. The game features a snake that grows as it consumes eggs and ends when the snake collides with itself or the boundaries of the screen.

## Features

- **Classic Snake Movement**: Control the snake to move up, down, left, or right.
- **Growing Mechanism**: The snake grows in length each time it eats an egg.
- **Collision Detection**: The game detects collisions with the screen boundaries and the snake itself.
- **Egg Respawn**: Eggs respawn at random locations on the screen after being eaten.
- **Score**: The score increases each time an egg is consumed.
- **Time Display**: Shows elapsed game time.
- **Game Over**: The game ends when the snake hits itself or the screen boundaries.
- **Restart Option**: After game over, you can choose to play again or exit.

## Requirements

- Python 3.12.4
- Pygame library

## Installation

To run this game, you'll need Python and Pygame installed. Follow these steps to set up the environment:

1. **Install Python**: Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Install Pygame**:
    If you haven't installed Pygame yet, you can do so using pip. If `pip` is not recognized, ensure that Python and pip are correctly installed and added to your system path.

    ```sh
    python -m pip install pygame
    ```

1. **Clone the repository**:
    Clone this repository to your local machine:
    ```sh
    git clone https://github.com/varunchithiraala/Snake-Game.git
    ```

## Running the Game

1. **Navigate to the game directory**:
    ```sh
    cd Snake-Game
    ```

2. **Run the game script**:
    Execute the snake_game.py file to start the game:
    ```sh
    python snake_game.py
    ```

## Controls

- **Arrow Keys**: Control the direction of the snake (Up, Down, Left, Right).
- **UP**: Move the snake up.
- **DOWN**: Move the snake down.
- **LEFT**: Move the snake left.
- **RIGHT**: Move the snake right.
- **ESCAPE**: Exit the game.
- **Y**: Play again after game over.
- **N**: Exit after game over.

## Files

- `snake_game.py`: The main Python script containing the game logic.
- `README.md`: This file.

## Contributing

Feel free to fork the repository and submit pull requests with improvements or bug fixes. Please make sure to follow the coding style and include appropriate tests for your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
