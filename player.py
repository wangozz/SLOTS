from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_tables import Player, Spin

engine = create_engine('sqlite:///slots_game.db')
Session = sessionmaker(bind=engine)

def get_player_data(identifier):
    session = Session()

    # Check if identifier is numeric 
    if identifier.isnumeric():
        player = session.query(Player).filter(Player.player_id == int(identifier)).first()
    else:
        player = session.query(Player).filter(Player.username == identifier).first()

    if player:
        print(f"Player ID: {player.player_id}")
        print(f"Username: {player.username}")
        print(f"Balance: {player.balance}")

        # retrieve the player's spin history
        spin_history = session.query(Spin).filter(Spin.player_id == player.player_id).all()

        if spin_history:
            print("\nSpin History:")
            for spin in spin_history:
                print(f"Spin ID: {spin.spin_id}")
                print(f"Result: {spin.result}")
                print(f"Bet Amount: {spin.bet_amount}")
                print(f"Timestamp: {spin.timestamp}")
                print("-" * 20)
        else:
            print("No spin history found for this player.")
    else:
        print(f"No player found with the identifier: {identifier}")

    session.close()

if __name__ == "__main__":
    player_input = input("Enter player name or ID: ")
    get_player_data(player_input)
