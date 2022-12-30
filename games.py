import random
import csv
from pathlib import Path
from sequences import Sequence, Row, SequenceValue
from lights import Light

def inorout(lights: list[Light], round_count: int) -> Sequence:
    # Create
    game = Sequence()
    game.name = "In or Out"
    
    for i in range(round_count):
        game_round = create_round(lights)
        game.rows.extend(game_round)
    
    return game


def create_round(lights: list[Light]) -> list[Row]:
    # Flash
    row_1 = set_all_row(lights, True, 0.5)
    row_2 = set_all_row(lights, False, 0.5)
    row_3 = set_all_row(lights, True, 0.5)
    row_4 = set_all_row(lights, False, 0.5)
    
    # All on while people choose
    row_5 = set_all_row(lights, True,6)
    
    # All on, except a random one is not
    result_row = set_all_row(lights, True,6)
    random_sequence_value = random.choice(result_row.values)
    random_sequence_value.state = False
    
    game_round = [
        row_1,
        row_2,
        row_3,
        row_4,
        row_5,
        result_row
    ]
    
    return game_round


def set_all_row(lights: list[Light], state: bool, time: float) -> Row:
    row = Row()
    row.time = time
    
    for light in lights:
        value = SequenceValue()
        value.light = light
        value.state = state
        row.values.append(value)
        
    return row