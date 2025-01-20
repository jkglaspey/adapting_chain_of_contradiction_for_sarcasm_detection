import os
import csv
from data_processing.text_utils import replace_emojis

class IACv2Reader:
    FILE_PATH_GEN = os.path.join(os.path.dirname(__file__), "../data/IAC-V2/GEN-sarc-notsarc.csv")
    FILE_PATH_HYP = os.path.join(os.path.dirname(__file__), "../data/IAC-V2/HYP-sarc-notsarc.csv")
    FILE_PATH_RQ = os.path.join(os.path.dirname(__file__), "../data/IAC-V2/RQ-sarc-notsarc.csv")

    @classmethod
    def read_data(cls, file_path: str) -> list[tuple[bool, str]]:
        """Reads data from the specified file path."""
        data = []

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 3:
                        try:
                            text = replace_emojis(row[2])  # Read text from the 3rd column
                            if row[0][0] == 's':  # First character of the first column
                                label = True
                            elif row[0][0] == 'n':
                                label = False
                            else:
                                raise ValueError("Line is in invalid format.")
                            data.append((label, text))
                        except ValueError as e:
                            print(f"Error parsing line {row}: {e}")
                    else:
                        print(f"Skipped malformed row: {row}")

        except FileNotFoundError:
            print(f"Error: File not found at {file_path}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        return data

    @classmethod
    def read_gen(cls) -> list[tuple[bool, str]]:
        """Reads data from the GEN file."""
        return cls.read_data(cls.FILE_PATH_GEN)

    @classmethod
    def read_hyp(cls) -> list[tuple[bool, str]]:
        """Reads data from the HYP file."""
        return cls.read_data(cls.FILE_PATH_HYP)

    @classmethod
    def read_rq(cls) -> list[tuple[bool, str]]:
        """Reads data from the RQ file."""
        return cls.read_data(cls.FILE_PATH_RQ)

    @classmethod
    def read_all(cls) -> list[tuple[bool, str]]:
        """Combines data from all three files into a single dataset."""
        all_data = []
        all_data.extend(cls.read_gen())
        all_data.extend(cls.read_hyp())
        all_data.extend(cls.read_rq())
        return all_data
