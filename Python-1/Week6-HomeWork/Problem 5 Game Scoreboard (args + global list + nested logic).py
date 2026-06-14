high_score_board = []
def record_game(player, *scores, bonus=0, multiplier=1.0):
    """
    Records a player's game results and updates the global leaderboard.
    
    Args:
        player (str): The name of the player.
        *scores (int): Variable number of round scores.
        bonus (int): Optional points to add. Defaults to 0.
        multiplier (float): Optional score multiplier. Defaults to 1.0.
    """
    if len(scores) == 0:
        return (player, 0, 0, "no rounds played")
    
    for s in scores:
        if s < 0:
            return (player, 0, 0, "negative score not allowed")
    
    raw_total = sum(scores)
    total = int((raw_total + bonus) * multiplier)
    rounds = len(scores)
    
    high_score_board.append((player, total))
    high_score_board.sort(key=lambda x: x[1], reverse=True)

    rank = 0
    for i, entry in enumerate(high_score_board):
        if entry[0] == player and entry[1] == total:
            rank = i + 1
            break
            
    status = "high score!" if rank == 1 else f"rank {rank}"
    
    return (player, rounds, total, status)

print(record_game("Omar", 50, 60, bonus=10))         
print(record_game("Ali", 100, 200, multiplier=1.5)) 
print(record_game("Sara", 30, 40, 50))              

print("\n--- Final Leaderboard ---")
for i, (name, score) in enumerate(high_score_board):
    print(f"{i+1}. {name}: {score}")