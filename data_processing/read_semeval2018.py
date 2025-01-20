import os
from data_processing.text_utils import replace_emojis

class SemEval2018Reader:
    FILE_PATH_TRAIN = os.path.join(os.path.dirname(__file__), "../data/SemEval2018Task3/train/SemEval2018-T3-train-taskA_emoji.txt")
    FILE_PATH_TEST = os.path.join(os.path.dirname(__file__), "../data/SemEval2018Task3/goldtest_TaskA/SemEval2018-T3_gold_test_taskA_emoji.txt")

    @classmethod
    def read_data(cls) -> list[tuple[bool, str]]:
        data = []

        try:
            # Process the training file
            with open(cls.FILE_PATH_TRAIN, 'r', encoding='utf-8') as file:
                for line_number, line in enumerate(file):
                    # Skip the first line
                    if line_number == 0:
                        continue

                    parts = line.strip().split('\t')
                    if len(parts) == 3:
                        text = replace_emojis(parts[2])
                        label = bool(int(parts[1]))
                        data.append((label, text))
                    else:
                        print(f"Skipped malformed line in TRAIN file: {line.strip()}")

            # Process the test file
            with open(cls.FILE_PATH_TEST, 'r', encoding='utf-8') as file:
                for line_number, line in enumerate(file):
                    # Skip the first line
                    if line_number == 0:
                        continue

                    parts = line.strip().split('\t')
                    if len(parts) == 3:
                        text = replace_emojis(parts[2])
                        label = bool(int(parts[1]))
                        data.append((label, text))
                    else:
                        print(f"Skipped malformed line in TEST file: {line.strip()}")

        except FileNotFoundError:
            print(f"Error: File not found at {cls.FILE_PATH_TRAIN} or {cls.FILE_PATH_TEST}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        return data
