from data_processing.read_ghosh import GhoshReader
from data_processing.read_iacv1 import IACv1Reader

class MainApp:
    def run(self, data_number: int):
        dataset_map = {
            0: self.read_ghosh,
            1: self.read_iacv1,
            2: self.read_iacv2,
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

        print(f"Parsed {len(data)} lines of data:\n")
        for idx, (label, text) in enumerate(data, start=1):
            print(f"{idx}. Label: {label}, Text: {text}")

    """
    Read in the IAC-V1 dataset
    """
    @staticmethod
    def read_iacv1():
        print("Reading data from IAC-V1 file...\n")
        data = IACv1Reader.read_data()
        data = IACv1Reader.shuffle_data()

        if not data:
            print("No data found or failed to read the file.")
            return

        print(f"Parsed {len(data)} lines of data:\n")
        for idx, (label, text) in enumerate(data, start=1):
            print(f"{idx}. Label: {label}, Text: {text}")

    """
    Read in the IAC-V2 dataset
    """
    @staticmethod
    def read_iacv2():
        print("Reading data from IAC-V2 dataset...")
        # Add logic to read IAC-V2 dataset
        return

    """
    Read in the iSarcasmEval dataset
    """
    @staticmethod
    def read_iSarcasmEval():
        print("Reading data from iSarcasmEval dataset...")
        # Add logic to read iSarcasmEval dataset
        return

    """
    Read in the SemEval 2018 Task 3 dataset
    """
    @staticmethod
    def read_semeval2018():
        print("Reading data from SemEval 2018 Task 3 dataset...")
        # Add logic to read SemEval 2018 dataset
        return


if __name__ == "__main__":
    """
    Determine which data to read corresponding to the number:
    0 = Ghosh
    1 = IAC-V1
    2 = IAC-V2
    3 = iSarcasmEval
    4 = SemEval2018Task3
    """
    data_number = 1  # Change this value to select the dataset

    # Execute the main logic
    app = MainApp()
    app.run(data_number)
