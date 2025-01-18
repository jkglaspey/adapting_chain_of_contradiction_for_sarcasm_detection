import emoji
import random

def replace_emojis(text: str) -> str:
    """
    Replace emojis with their descriptive tags, prefixed with '#'.
    Example: 😂 becomes #facewithtears.
    """
    result = []
    for char in text:
        if emoji.is_emoji(char):  # Check if the character is an emoji
            description = emoji.demojize(char).strip(':').replace('_', '')
            result.append(f"#{description}")
        else:
            result.append(char)
    return ''.join(result)


def shuffle_data(FILE_PATH: str, SHUFFLED_FILE_PATH: str):
    try:
        # Read the lines from data.txt
        with open(FILE_PATH, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Shuffle the lines randomly
        random.shuffle(lines)

        # Write the shuffled lines to a new file
        with open(SHUFFLED_FILE_PATH, 'w', encoding='utf-8') as output_file:
            output_file.writelines(lines)

        print(f"Data successfully shuffled and written to {SHUFFLED_FILE_PATH}")

    except FileNotFoundError:
        print(f"Error: {FILE_PATH} not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")