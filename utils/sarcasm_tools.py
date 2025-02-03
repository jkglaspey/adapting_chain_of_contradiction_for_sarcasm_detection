@staticmethod
def is_sarcastic(response: str) -> bool:

    normalized_response = response.strip().lower()
    
    if "not sarcastic" in normalized_response:
        return False
    elif "sarcastic" in normalized_response:
        return True
    else:
        raise ValueError(f"Unexpected response: '{response}'")