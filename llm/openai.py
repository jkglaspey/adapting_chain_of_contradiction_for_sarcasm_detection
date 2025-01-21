import openai
from ..utils.constants.llmprompts import CoCPrompts
from ..utils.sarcasm_tools import is_sarcastic

# Turn on debugging mode
debug = True

def start_conversation_with_gpt(iterable_list):

    # Returned list of "sarcastic" versus "non-sarcastic"
    res = []

    for label, item in iterable_list:
        if debug:
            print(f"Starting conversation for item: {item}")

        # Step 1: Start the conversation and ask the first question
        updated_prompt = CoCPrompts[0].replace("$X$", item)
        first_response = chat_with_gpt(updated_prompt)
        if debug:
            print(f"GPT Response 1: {first_response}")

        # Step 2: Ask the second question, using the first response
        second_question = CoCPrompts[1]
        second_response = chat_with_gpt(second_question, previous_responses=[first_response])
        if debug:
            print(f"GPT Response 2: {second_response}")

        # Step 3: Ask the third question, using the second response
        third_question = CoCPrompts[2]
        third_response = chat_with_gpt(third_question, previous_responses=[first_response, second_response])
        if debug:
            print(f"GPT Response 3: {third_response}")

        # Step 4: Determine if the output is labeled as "Sarcastic" or "Not Sarcastic." If not, query to fix it.
        try:
            res.append(is_sarcastic(third_response))
        
        # Step 5 (optional): Requery if the LLM failed to format correctly.
        except ValueError as e:
            fourth_response = chat_with_gpt(third_question, previous_responses=[first_response, second_response, third_response])
            if debug:
                print(f"GPT Response 4: {fourth_response}")
            try:
                res.append(is_sarcastic(third_response))

            # Fail case: GPT did not format correctly
            except ValueError as e:
                res.append(-1)
                print(f"GPT could not format a response for {item}")

        if debug:
            print("-" * 50)

    return res
            

def chat_with_gpt(question, previous_responses=None):
    messages = [{"role": "system", "content": "You are a helpful assistant."}]

    if previous_responses:
        for response in previous_responses:
            messages.append({"role": "assistant", "content": response})

    messages.append({"role": "user", "content": question})

    # Query GPT
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )

    # Extract and return the text response
    return response["choices"][0]["message"]["content"].strip()


def initialize_chat_with_gpt(iterable_list, api_key: str):
    # Set your OpenAI API key
    openai.api_key = api_key

    return start_conversation_with_gpt(iterable_list)