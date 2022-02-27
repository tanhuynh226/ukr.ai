import os
from dotenv import load_dotenv
import openai
from transformers import GPT2TokenizerFast
import numpy as np
from collections import defaultdict

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
labels = ["NOT_MISLEADING", "MISINFORMED_OR_POTENTIALLY_MISLEADING"]
labels = [label.strip().lower().capitalize() for label in labels]
labels_tokens = {label: tokenizer.encode(" " + label) for label in labels}

def answer(prompt):
    response = openai.Classification.create(
    file = "file-R5VA59nOEqhU4L0QgR3EyGTK",
    query = prompt,
    search_model = "curie", 
    model = "curie", 
    labels = labels,
    logprobs = 3,
    max_examples = 1000)

    first_token_to_label = {
        tokenizer.decode([tokens[0]]).strip().lower(): label 
        for label, tokens in labels_tokens.items()
    }

    top_logprobs = response["completion"]["choices"][0]["logprobs"]["top_logprobs"][0]
    token_probs = defaultdict(float)
    for token, logp in top_logprobs.items():
        token_probs[token.strip().lower()] += np.exp(logp)

    label_probs = {
        first_token_to_label[token]: prob 
        for token, prob in token_probs.items()
        if token in first_token_to_label
    }

    # Fill in the probability for the special "Unknown" label.
    if sum(label_probs.values()) < 1.0:
        label_probs["Unknown"] = 1.0 - sum(label_probs.values())

    label_probs['label'] = response['label']
    # print(label_probs)

    # print(response['label'])

    return label_probs

# nobirdwatch training : file-5tWsG9oQZyrIW5JGt6YvKas3
# birdwatch + manual training : file-R5VA59nOEqhU4L0QgR3EyGTK
# patrick : file-i5K6dpIvAcYzNDDUW60bX6Kn

def main():
    response = openai.Classification.create(
    file = "file-d9g34SRx4Vd0aJkJkNZs1dId",
    query = "There weren't any reports of explosions in Kiev.",
    search_model = "curie", 
    model = "ada", 
    labels = labels,
    logprobs = 3,
    max_examples = 200)

    first_token_to_label = {
        tokenizer.decode([tokens[0]]).strip().lower(): label 
        for label, tokens in labels_tokens.items()
    }

    top_logprobs = response["completion"]["choices"][0]["logprobs"]["top_logprobs"][0]
    token_probs = defaultdict(float)
    for token, logp in top_logprobs.items():
        token_probs[token.strip().lower()] += np.exp(logp)

    label_probs = {
        first_token_to_label[token]: prob 
        for token, prob in token_probs.items()
        if token in first_token_to_label
    }

# Fill in the probability for the special "Unknown" label.
    if sum(label_probs.values()) < 1.0:
        label_probs["Unknown"] = 1.0 - sum(label_probs.values())

    label_probs['label'] = response['label']
    print(label_probs)
    
    # print(response['label'])

if __name__ == "__main__":
    main()

