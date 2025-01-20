import random

def shuffle_txt(input_file: str, output_file: str):
    # Read all lines from the input file
    with open(input_file, mode='r', encoding='utf-8') as file:
        lines = file.readlines()

    # Shuffle the lines
    random.shuffle(lines)

    # Write the shuffled lines to the output file
    with open(output_file, mode='w', encoding='utf-8') as file:
        file.writelines(lines)

if __name__ == "__main__":
    # Example usage
    input_txt = 'data.txt'       # Replace with your input file name
    output_txt = 'shuffled.txt'   # Replace with your desired output file name

    shuffle_txt(input_txt, output_txt)
    print(f"The shuffled file has been saved to '{output_txt}'")
