def setmode(board: str):
    print(f"Set mode to {board}")

def setup(pin: int, type: str):
    print(f"Setup pin {pin} to {type}")

def output(pin: int, value: str):
    print(f"Set pin {pin} to {value}")

def cleanup():
    print("Clean up GPIO")

BOARD = "BOARD"
OUT = "OUT"
LOW = "LOW"
HIGH = "HIGH"