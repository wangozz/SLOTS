from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_tables import History

engine = create_engine('sqlite:///slots_game.db')
Session = sessionmaker(bind=engine)

def kill(player_id):
    session = Session()
    
    # Query the history record by player_id
    history_record = session.query(History).filter(History.player_id == player_id).first()

    if history_record:
        # Delete the history record
        session.delete(history_record)
        session.commit()
        print(f"Player history with ID {player_id} has been deleted.")
    else:
        print(f"No history found for player with ID {player_id}.")

    session.close()

if __name__ == "__main__":
    player_id_to_delete = int(input("Enter the player ID whose history you want to delete: "))
    kill(player_id_to_delete)
