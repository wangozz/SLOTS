import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_tables import Player, Spin, History

engine = create_engine('sqlite:///slots_game.db')
Session = sessionmaker(bind=engine)

def pull_lever():
    symbols = [5, 6, 7, 8, 9]
    result = [random.choice(symbols) for _ in range(3)]
    return result

def play_slots(player_name, num_spins, bet_amount, starter_tokens):
    print(f"Welcome to the Slots game, {player_name}!")


    session = Session()
    player = session.query(Player).filter(Player.username == player_name).first()

    if not player:
        player = Player(username=player_name, balance=starter_tokens)
        session.add(player)

    session.commit()

    for _ in range(num_spins):
        print(f"\nSpin {_+1}:")
        result = pull_lever()
        print(f"Result: {result[0]} | {result[1]} | {result[2]}")

        if result == [7, 7, 7]:
            print("Congratulations! You won the jackpot!")
            player.balance += (bet_amount * 2) - bet_amount  # Double balance on jackpot

        else:
            player.balance -= bet_amount  # Subtract bet amount if no jackpot

        spin = Spin(player=player, result=str(result), bet_amount=bet_amount)
        session.add(spin)

        player_id = player.player_id

        history = History(player_id=player_id, username=player.username, spins=num_spins, balance=player.balance)
        session.add(history)

    session.commit()
    session.close()

if __name__ == "__main__":
    player_name = input("Enter your name: ")
    print("You have received 10000 tokens as a starter bet amount.")
    bet_amount = float(input("Enter your stake: "))
    num_spins = int(input("How many times would you like to spin? "))

    starter_tokens = 10000
    play_slots(player_name, num_spins, bet_amount, starter_tokens)
