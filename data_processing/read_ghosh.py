import os
from data_processing.text_utils import replace_emojis

class GhoshReader:
    FILE_PATH = os.path.join(os.path.dirname(__file__), "../data/Ghosh/data.txt")

    @classmethod
    def read_data(cls) -> list[tuple[bool, str]]:
        data = []

        try:
            with open(cls.FILE_PATH, 'r', encoding='utf-8') as file:
                for line in file:
                    parts = line.strip().split('\t')
                    
                    if len(parts) == 3:
                        text = replace_emojis(parts[2])
                        label = bool(int(parts[1]))
                        data.append((label, text))
                    else:
                        print(f"Skipped malformed line: {line.strip()}")

        except FileNotFoundError:
            print(f"Error: File not found at {cls.FILE_PATH}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        return data