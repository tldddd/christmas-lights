import csv
from pathlib import Path
from lights import Light


class Sequence:
    def __init__(self) -> None:
        self.name: str = ""  # This is the file name.
        self.rows: list[Row] = []


class Row:
    def __init__(self) -> None:
        self.time: float = 0
        self.values: list[SequenceValue] = []


class SequenceValue:
    def __init__(self) -> None:
        self.light: Light = None
        self.state: bool = False


def load_sequences(lights: list[Light]) -> list[Sequence]:
    folder_path = Path("sequences").absolute()
    sequence_files = list(folder_path.glob("*.csv"))

    sequences: list[Sequence] = []

    for sequence_file in sequence_files:
        try:
            seq = read_sequence_file(sequence_file, lights)
            sequences.append(seq)
        except Exception as e:
            print(f"Unable to read {sequence_file.stem}")

    return sequences


def read_sequence_file(file_path: Path, lights: list[Light]) -> Sequence:
    sequence = Sequence()
    sequence.name = file_path.stem

    with open(file_path) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=",")
        for csv_row in csv_reader:
            row = to_row(csv_row, lights)
            sequence.rows.append(row)

    return sequence


def to_row(csv_row: dict[str, str], lights: list[Light]) -> Row:
    row = Row()
    row.time = float(csv_row["time"])

    for key, value in csv_row.items():
        if key == "time":
            continue

        seq_value = SequenceValue()

        if value.lower() == "true":
            seq_value.state = True

        light = [l for l in lights if l.seq_code == key][0]
        seq_value.light = light

        row.values.append(seq_value)

    return row
