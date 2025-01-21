@staticmethod
def is_sarcastic(response: str) -> bool:

    normalized_response = response.strip().lower()
    
    if "sarcastic" in normalized_response:
        return 1
    elif "not sarcastic" in normalized_response:
        return 0
    else:
        raise ValueError(f"Unexpected response: '{response}'")