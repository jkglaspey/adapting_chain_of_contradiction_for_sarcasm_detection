from functools import partial
import argparse
from data_processing.read_ghosh import GhoshReader
from data_processing.read_iacv1 import IACv1Reader
from data_processing.read_iacv2 import IACv2Reader
from data_processing.read_isarcasmeval import ISarcasmEvalReader
from data_processing.read_semeval2018 import SemEval2018Reader
from data_processing.read_testdata import TestDataReader
from llm.openai import initialize_chat_with_gpt


class MainApp:
    def run(self, data_number: int, datatype_number: int, llm_number: int, api_key: str):
        dataset_map = {
            0: self.read_ghosh,
            1: self.read_iacv1,
            2: partial(self.read_iacv2, datatype_number=datatype_number),
            3: self.read_iSarcasmEval,
            4: self.read_semeval2018,
            5: self.read_testdata
        }

        # Retrieve and call the corresponding method, or handle invalid numbers
        get_data = dataset_map.get(data_number)
        if get_data:
            data = get_data()

            if data == -1:
                return

            #for idx, (label, text) in enumerate(data, start=1):
            #    print(f"{idx}. Label: {label}, Text: {text}")
            print(f"Parsed {len(data)} lines of data:\n")
        else:
            print(f"Error: Invalid method number '{data_number}'. Please choose between 0 and 5.")
            return

        # Data is a 2D array
        # 1. Bool (True = sarcastic, False = not sarcastic)
        # 2. Text

        llm_map = {
            0: self.chat_gpt,
            1: self.chat_claude,
            2: self.chat_llama,
            3: self.chat_bert,
            4: self.chat_deberta
        }

        # Write the header
        filename = f"results_dataset{data_number}_llm{llm_number}.txt"
        TP = FP = TN = FN = 0
        with open(filename, "a") as file:
            # Write header information
            if file.tell() == 0:
                file.write(f"------------------\nDataset Number: {data_number}\n")
                file.write(f"LLM Model Used: {llm_number}\n")
                file.write(f"Number of Samples Evaluated: {(len(data))}\n")
                file.write("\nResults:\n")
                file.write("Data Label\tLLM Label\n")

        # Retrieve and call the corresponding LLM
        TP = TN = FP = FN = 0
        if llm_number in llm_map:
            # Call the function and store the result
            TP, TN, FP, FN = llm_map[llm_number](data, api_key, filename)
        else:
            print(f"Error: Invalid llm number '{llm_number}'. Please choose between 0 and 4.")
            return

    """
    Read in the Ghosh dataset
    """
    @staticmethod
    def read_ghosh():
        print("Reading data from Ghosh file...\n")
        data = GhoshReader.read_data()

        if not data:
            print("No data found or failed to read the file.")
            return -1

        return data

    """
    Read in the IAC-V1 dataset
    """
    @staticmethod
    def read_iacv1():
        print("Reading data from IAC-V1 file...\n")
        data = IACv1Reader.read_data()

        if not data:
            print("No data found or failed to read the file.")
            return -1

        return data

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
            return -1

        return data

    """
    Read in the iSarcasmEval dataset
    """
    @staticmethod
    def read_iSarcasmEval():
        print("Reading data from iSarcasmEval dataset...")
        data = ISarcasmEvalReader.read_data()

        if not data:
            print("No data found or failed to read the file.")
            return -1

        return data

    """
    Read in the SemEval 2018 Task 3 dataset
    """
    @staticmethod
    def read_semeval2018():
        print("Reading data from SemEval 2018 Task 3 dataset...")
        data = SemEval2018Reader.read_data()

        if not data:
            print("No data found or failed to read the file.")
            return -1

        return data

    """
    Read in the Test dataset
    """
    @staticmethod
    def read_testdata():
        print("Reading data from Test Dataset...\n")
        data = TestDataReader.read_data()

        if not data:
            print("No data found or failed to read the file.")
            return -1

        return data

    
    """
    Converse with ChatGPT
    """
    @staticmethod
    def chat_gpt(data, api_key, filename):

        # Returns list of True/False/-1, 
        # True = Sarcastic, 
        # False = Non-sarcastic. 
        # -1 = Could not parse.
        # In the same order as input data.
        return initialize_chat_with_gpt(data, api_key, filename)
    
    """
    Converse with Claude
    """
    @staticmethod
    def chat_claude(data):
        return
    
    """
    Converse with LLaMa 3
    """
    @staticmethod
    def chat_llama(data):
        return
    
    """
    Converse with BERT
    """
    @staticmethod
    def chat_bert(data):
        return
    
    """
    Converse with DeBERTa
    """
    @staticmethod
    def chat_deberta(data):
        return


if __name__ == "__main__":
    """
    Determine which data to read corresponding to the number:
    0 = Ghosh
    1 = IAC-V1
    2 = IAC-V2
    3 = iSarcasmEval
    4 = SemEval2018Task3
    5 = Test Dataset
    """

    # Scan in input parameters
    parser = argparse.ArgumentParser(description="Allow the user to configure parameters directly in the command line.")
    parser.add_argument("--dataset_number", required=True, help="Select the correct dataset. 0 = Ghosh, 1 = IAC-V1, 2 = IAC-V2, 3 = iSarcasmEval, 4 = SemEval2018Task3, 5 = Test Dataset")
    parser.add_argument("--llm_number", required=True, help="Select the LLM to converse to. 0 = GPT, 1 = Claude, 2 = LLaMa 3, 3 = BERT, 4 = DeBERTa")
    parser.add_argument("--api_key", required=True, help="Your OpenAI API key")
    args = parser.parse_args()

    # Configure input parameters
    api_key = args.api_key
    data_number = int(args.dataset_number)
    llm_number = int(args.llm_number)
    datatype_number = 1     # Don't change this unless experimenting.

    # Execute the main logic
    app = MainApp()
    app.run(data_number, datatype_number, llm_number, api_key)
