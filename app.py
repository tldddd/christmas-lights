import time
import multiprocessing
from multiprocessing import Process

from pathlib import Path

from lights import Light, load_lights, on, off, setup_pins, setup_gpio
from sequences import Sequence, load_sequences
from games import inorout


class App:
    def __init__(self) -> None:
        # Problem is, I want to be playing a sequence.
        # How to kill it at any point?
        # Create an app, pass it to the
        setup_gpio()
        self.lights = load_lights()
        setup_pins(self.lights)
        self.sequences = load_sequences(self.lights)

        self.current_sequence_process: Process = None

    def get_lights(self) -> list[Light]:
        return self.lights

    def get_sequences(self) -> list[Sequence]:
        # sequence_names = [s.name for s in self.sequences]
        return self.sequences

    def set_light(self, id: int, state: bool) -> Light:
        # Stop any current seq
        self.stop_current_seq()

        matching_lights = [l for l in self.lights if l.id == id]
        light = matching_lights[0]

        if state == True:
            on(light)

        if state == False:
            off(light)

        return light
    
    def game_inorout(self) -> Sequence:
        # Only certain lights are used
        print("Start game In Or Out")
        codes = ["cc", "ws", "hh", "li", "sm"]
        lights_in_play = [l for l in self.lights if l.seq_code in codes]
        print(f"Got {len(lights_in_play)} lights in play")
        
        game_seq = inorout(lights_in_play, 50)
        
        print("Sequence made, starting game...")
        return self.start_seq_direct(game_seq)

    def start_seq(self, name: str) -> Sequence:
        matching_seq = [l for l in self.sequences if l.name == name]
        seq = matching_seq[0]
        
        return self.start_seq_direct(seq)
        
        
    def start_seq_direct(self, seq: Sequence) -> Sequence:
        self.stop_current_seq()

        arg = [seq]

        proc = multiprocessing.Process(target=self.run_sequence, args=arg)
        self.current_sequence_process = proc
        proc.start()

        print(f"Started sequence {seq.name}")
        return seq

    def run_sequence(self, seq: Sequence):
        # run the sequence forever
        row_index = 0

        while True:
            row = seq.rows[row_index]

            print(f"Doing row {row_index}")

            # Set all the lights.
            for v in row.values:
                # Don't change if already that state.
                if v.state == v.light.state:
                    continue
                if v.state == True:
                    on(v.light)

                if v.state == False:
                    off(v.light)

            # Then stop
            wait = row.time
            time.sleep(wait)

            row_index = row_index + 1

            # Restart if we've reached the end.
            if row_index == len(seq.rows):
                row_index = 0

    def stop_current_seq(self):
        if self.current_sequence_process is None:
            return

        print("Stopping current sequence.")
        self.current_sequence_process.terminate()
