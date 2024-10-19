import random

HEADS = "heads"
TAILS = "tails"
COIN_VALUE = [HEADS, TAILS]


def flip_coin():
    return random.choice(COIN_VALUE)


def play_martingale(*, starting_founds: int, min_bet: int, max_bet: int) -> int:
    steps_to_loose = 0
    current_funds = starting_founds
    current_bet = min_bet

    while current_funds > 0:
        # print("======")
        steps_to_loose += 1
        current_funds -= current_bet
        # print(f"{current_funds=}, {current_bet=}")
        flipped_coin_value = flip_coin()

        if flipped_coin_value == HEADS:
            winner = current_bet * 2
            # print(f"{winner=}")
            current_funds += winner
            current_bet = min_bet
        else:
            # print("loose")
            current_bet *= 2
            if current_bet > max_bet:
                current_bet = min_bet
            if current_bet > current_funds:
                current_bet = current_funds

    return steps_to_loose


# print(play_martingale(starting_founds=100, min_bet=1, max_bet=100))

def simulate_martingale_for_n_players(*, starting_founds: int, min_bet: int, max_bet: int, n_games: int) -> float:
    total_steps_to_loose = 0
    for i in range(n_games):
        step_to_loose = play_martingale(starting_founds=starting_founds, min_bet=min_bet, max_bet=max_bet)
        total_steps_to_loose += step_to_loose

    return total_steps_to_loose / n_games


print(simulate_martingale_for_n_players(
    n_games=10,
    starting_founds=1000,
    min_bet=1,
    max_bet=100
))