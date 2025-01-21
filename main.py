from functools import partial
import argparse
from data_processing.read_ghosh import GhoshReader
from data_processing.read_iacv1 import IACv1Reader
from data_processing.read_iacv2 import IACv2Reader
from data_processing.read_isarcasmeval import ISarcasmEvalReader
from data_processing.read_semeval2018 import SemEval2018Reader


class MainApp:
    def run(self, data_number: int, datatype_number: int):
        dataset_map = {
            0: self.read_ghosh,
            1: self.read_iacv1,
            2: partial(self.read_iacv2, datatype_number=datatype_number),
            3: self.read_iSarcasmEval,
            4: self.read_semeval2018,
        }

        # Retrieve and call the corresponding method, or handle invalid numbers
        get_data = dataset_map.get(data_number)
        if get_data:
            data = get_data()
        else:
            print(f"Error: Invalid method number '{data_number}'. Please choose between 0 and 4.")

        # Data is a 2D array
        # 1. Bool (True = sarcastic, False = not sarcastic)
        # 2. Text

    """
    Read in the Ghosh dataset
    """
    @staticmethod
    def read_ghosh():
        print("Reading data from Ghosh file...\n")
        data = GhoshReader.read_data()

        if not data:
            print("No data found or failed to read the file.")
            return

        for idx, (label, text) in enumerate(data, start=1):
            print(f"{idx}. Label: {label}, Text: {text}")
        print(f"Parsed {len(data)} lines of data:\n")

    """
    Read in the IAC-V1 dataset
    """
    @staticmethod
    def read_iacv1():
        print("Reading data from IAC-V1 file...\n")
        data = IACv1Reader.read_data()

        if not data:
            print("No data found or failed to read the file.")
            return

        for idx, (label, text) in enumerate(data, start=1):
            print(f"{idx}. Label: {label}, Text: {text}")
        print(f"Parsed {len(data)} lines of data:\n")

    """
    Read in the IAC-V2 dataset
    """
    @staticmethod
    def read_iacv2(datatype_number: int):
        print(f'Using datatype: {datatype_number} --> Reading data from IAC-V2 dataset...')

        # Datatype assignment
        # 0 = All groups
        # 1 = General
        # 2 = Hyperbole
        # 3 = Rhetorical Questions
        datatype_map = {
            0: IACv2Reader.read_all,
            1: IACv2Reader.read_gen,
            2: IACv2Reader.read_hyp,
            3: IACv2Reader.read_rq,
        }

        # Retrieve and call the corresponding method, or handle invalid numbers
        get_datatype = datatype_map.get(datatype_number)
        if get_datatype:
            data = get_datatype()
        else:
            print(f"Error: Invalid method number '{datatype_number}'. Please choose between 0 and 3.")

        if not data:
            print("No data found or failed to read the file.")
            return

        for idx, (label, text) in enumerate(data, start=1):
            print(f"{idx}. Label: {label}, Text: {text}")
        print(f"Parsed {len(data)} lines of data:\n")

    """
    Read in the iSarcasmEval dataset
    """
    @staticmethod
    def read_iSarcasmEval():
        print("Reading data from iSarcasmEval dataset...")
        data = ISarcasmEvalReader.read_data()

        if not data:
            print("No data found or failed to read the file.")
            return

        for idx, (label, text) in enumerate(data, start=1):
            print(f"{idx}. Label: {label}, Text: {text}")
        print(f"Parsed {len(data)} lines of data:\n")

    """
    Read in the SemEval 2018 Task 3 dataset
    """
    @staticmethod
    def read_semeval2018():
        print("Reading data from SemEval 2018 Task 3 dataset...")
        data = SemEval2018Reader.read_data()

        if not data:
            print("No data found or failed to read the file.")
            return

        for idx, (label, text) in enumerate(data, start=1):
            print(f"{idx}. Label: {label}, Text: {text}")
        print(f"Parsed {len(data)} lines of data:\n")


if __name__ == "__main__":
    """
    Determine which data to read corresponding to the number:
    0 = Ghosh
    1 = IAC-V1
    2 = IAC-V2
    3 = iSarcasmEval
    4 = SemEval2018Task3
    """

    # Scan in input parameters
    parser = argparse.ArgumentParser(description="Allow the user to configure parameters directly in the command line.")
    parser.add_argument("--dataset_number", required=True, help="Select the correct dataset. 0 = Ghosh, 1 = IAC-V1, 2 = IAC-V2, 3=iSarcasmEval, 4 = SemEval2018Task3")
    parser.add_argument("--api_key", required=True, help="Your OpenAI API key")
    args = parser.parse_args()

    # Configure input parameters
    openai_api_key = args.api_key
    data_number = args.dataset_number
    datatype_number = 1     # Don't change this unless experimenting.

    # Execute the main logic
    app = MainApp()
    app.run(data_number, datatype_number)
