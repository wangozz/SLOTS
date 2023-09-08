# SLOTS
# Slot Machine Game

Welcome to the Slot Machine Game project! This Python-based game allows players to spin the slot machine and try to match the jackpot combination (777). The project utilizes SQLAlchemy for database interactions to record player and spin data.

## Features

- Players can spin the slot machine and try to match the jackpot combination (777).
- Players receive a starter bet amount of 10000 tokens.
- The bet amount is subtracted from the starter tokens.
- If a player wins the jackpot, their balance is doubled.
- Player and spin data are recorded in the database.

## Getting Started

1. **Clone the Repository**:

git clone https://github.com/wangozz/SLOTS.git


2. **Install Dependencies**:

pip install sqlalchemy


3. **Create Database Tables**:

python create_tables.py


## Playing the Game

To play the game, run the `slots_game.py` script:

python slots_game.py


Follow the prompts to enter your name, bet amount, and the number of spins you'd like to make.

## Viewing Player Data

To view player data by either name or ID, you can use the `player.py` script:

python player.py


Follow the prompts to enter the player name or ID you want to search for.

## Deleting Player History

You can delete a player's history by ID using the `kill` function in `player.py`. Follow the prompts to enter the player ID you want to delete.

## Files

- `create_tables.py`: Defines the database tables and sets up the database.
- `slots_game.py`: Contains the game logic and interaction with the database.
- `player.py`: Allows searching for player data by name or ID and deleting player history.
- `README.md`: This file.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request with your changes.

