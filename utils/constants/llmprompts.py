CoCPrompts = [
    "Given the input sentence [$X$], what is the SURFACE sentiment, as indicated by clues such as keywords, sentimental phrases, emojis? Make your answer concise.",
    "Deduce what the sentence really means, namely the TRUE intention, by carefully checking any rhetorical devices, language style, unusual punctuations, common senses. Make your answer concise.",
    "Based on Step 1 and Step 2, evaluate whether the surface sentiment aligns with the true intention. If they do not match, the sentence is probably ‘Sarcastic’. Otherwise, the sentence is ‘Not Sarcastic’. Return the label only.",
    "Based on the conversation history, say ONLY the label 'sarcastic' or 'not-sarcastic'. If you think it is sarcastic, reply 'sarcastic'. If you think it is not sarcastic, reply 'not sarcastic'. Do not include any other text or symbols, including ''."
]

CoTPrompts = {
# Evaluate this later if time permits. Utilize converting
# inputs to vectors and computing cosine similarity to
# select the k nearest neighbors. This was done with
# k = 2, 4, 6, 8.
}

GoCPrompts = {
# Introduct graph of cueues later if time permits.
}