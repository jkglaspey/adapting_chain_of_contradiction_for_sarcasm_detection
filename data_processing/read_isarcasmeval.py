import os
import csv
from data_processing.text_utils import replace_emojis

class ISarcasmEvalReader:
    FILE_PATH_TEST = os.path.join(os.path.dirname(__file__), "../data/iSarcasmEval/task_A_En_test.csv")

    @classmethod
    def read_data(cls) -> list[tuple[bool, str]]:
        data = []

        try:
            with open(cls.FILE_PATH_TEST, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 2:
                        try:
                            text = replace_emojis(row[0])
                            label = bool(int(row[1]))
                            data.append((label, text))
                        except ValueError as e:
                            print(f"Error parsing line {row}: {e}")
                    else:
                        print(f"Skipped malformed row: {row}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        return data
