from openai import OpenAI
from utils.constants.llmprompts import CoCPrompts
from utils.sarcasm_tools import is_sarcastic
from utils.calc_metric import calc_acc, calc_F1, calc_precision, calc_recall


# Turn on debugging mode
debug = False

def start_conversation_with_gpt(iterable_list, api_key_var: str, filename: str):

    # Set your OpenAI API key
    client = OpenAI(
        api_key=api_key_var
    )

    # Define variables
    TP = 8822
    TN = 5673
    FP = 4477
    FN = 26
    start_idx = 18999
    length_list = len(iterable_list)

    for idx, (label, item) in enumerate(iterable_list[(start_idx - 1):], start=start_idx):
        print(f"{idx}/{length_list}: Starting conversation for item: {item}")
        res = -1

        # Step 1: Start the conversation and ask the first question
        updated_prompt = CoCPrompts[0].replace("$X$", item)
        first_response = chat_with_gpt(client, updated_prompt)
        if debug:
            print(f"GPT Response 1: {first_response}")

        # Step 2: Ask the second question, using the first response
        second_question = CoCPrompts[1]
        second_response = chat_with_gpt(client, second_question, previous_responses=[updated_prompt, first_response])
        if debug:
            print(f"GPT Response 2: {second_response}")

        # Step 3: Ask the third question, using the second response
        third_question = CoCPrompts[2]
        third_response = chat_with_gpt(client, third_question, previous_responses=[updated_prompt, first_response, second_question, second_response])
        if debug:
            print(f"GPT Response 3: {third_response}")

        # Step 4: Determine if the output is sarcastic or not
        try:
            res = is_sarcastic(third_response)
        
        except ValueError as e:
            # Step 5: Requery if LLM failed to format correctly
            fourth_question = CoCPrompts[3]
            fourth_response = chat_with_gpt(client, fourth_question, previous_responses=[updated_prompt, first_response, second_question, second_response, third_question, third_response])
            if debug:
                print(f"GPT Response 4: {fourth_response}")
            try:
                res = is_sarcastic(fourth_response)
            except ValueError:
                res = -1  # Mark as -1 if LLM could not handle it
                print(f"GPT could not format a response for {item}")
            
        # Step 6: Write to file
        with open(filename, "a") as file:
            if res == -1:
                file.write(f"{label}\tNULL\n")
                continue
            file.write(f"{label}\t{res}\t\t")

        # Step 7: Update metrics
        if label and res == True:
            TP += 1
        elif label and res == False:
            FN += 1
        elif not label and res == False:
            TN += 1
        elif not label and res == True:
            FP += 1
        with open(filename, "a") as file:
            file.write(f"{idx}. (TP = {TP}, FP = {FP}, TN = {TN}, FN = {FN})\n")

        if debug:
            print("-" * 50)

    return TP, TN, FP, FN


def chat_with_gpt(client, question, previous_responses=None):
    messages = [{"role": "system", "content": "You are a helpful assistant."}]

    if previous_responses:
        flag = True
        for response in previous_responses:
            if flag:
                messages.append({"role": "user", "content": response})
            else:
                messages.append({"role": "assistant", "content": response})
            flag = not flag

    messages.append({"role": "user", "content": question})

    # Query GPT
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_completion_tokens = 150
    )

    # Extract and return the text response
    return completion.choices[0].message.content


def initialize_chat_with_gpt(iterable_list, api_key_var: str, filename: str):

    TP, TN, FP, FN = start_conversation_with_gpt(iterable_list, api_key_var, filename)

    # After the loop, append metrics to the file
    with open(filename, "a") as file:
        file.write("\nMetrics:\n")
        precision = calc_precision(TP, FP)
        recall = calc_recall(TP, FN)
        f1 = calc_F1(precision, recall)
        accuracy = calc_acc(TP, TN, FP, FN)

        file.write(f"True Positives (TP): {TP}\n")
        file.write(f"False Positives (FP): {FP}\n")
        file.write(f"False Negatives (FN): {FN}\n")
        file.write(f"True Negatives (TN): {TN}\n")
        file.write(f"Precision: {precision:.4f}\n")
        file.write(f"Recall: {recall:.4f}\n")
        file.write(f"F1 Score: {f1:.4f}\n")
        file.write(f"Accuracy: {accuracy:.4f}\n")

    print(f"Results saved to {filename}")

    return TP, TN, FP, FN
