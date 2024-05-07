totalMetres = 100

player_1 = {
    "name": "juan",
    "metre": 40,
    "vel": 5
}

player_2 = {
    "name": "fede",
    "metre": 40,
    "vel": 5
}

player_1_remaining_time = (totalMetres - player_1["metre"]) / player_1["vel"]
player_2_remaining_time = (totalMetres - player_2["metre"]) / player_2["vel"]



if player_1_remaining_time < player_2_remaining_time:
    print("Player 1 wins")
elif player_1_remaining_time == player_2_remaining_time:
    print("Tie")
else:
    print("Player 2 wins")

