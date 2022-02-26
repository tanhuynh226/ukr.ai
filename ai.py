import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# openai.File.create(
#   file=open("training_data_prepared.jsonl", encoding='utf-8'),
#   purpose='classifications')

# openai.File.delete("file-Wi2EarKvIVyLigxmgBxkEnA6")

# print(openai.File.list())

def answer(prompt):
    response = openai.Classification.create(
    file = "file-ONAi4SXDpEUAdC3YaCtB2ZB9",
    query = prompt,
    search_model = "ada", 
    model = "curie", 
    labels = ["NOT_MISLEADING", "MISINFORMED_OR_POTENTIALLY_MISLEADING"],
    max_examples = 200)

    # print(response['label'])

    return response['label']

def main():
    response = openai.Classification.create(
    file = "file-pLp74SVfdDJsyvTAen8ZZeD2",
    query = "Russia plans to kill any Ukrainians that refuse to surrender",
#     examples = [
#         ["Ukraine did not start the conflict with Russia.", "NOT_MISLEADING"],
#         ["Russia wanted to fight Ukraine.", "NOT_MISLEADING"],
#         ["Ukraine initiated the conflict with Russia.", "MISINFORMED_OR_POTENTIALLY_MISLEADING"],
#         ["Russia initiated the conflict with Ukraine.", "NOT_MISLEADING"]
#     ],
    search_model = "ada", 
    model = "curie", 
    labels = ["NOT_MISLEADING", "MISINFORMED_OR_POTENTIALLY_MISLEADING"],
    max_examples = 200)
    
    print(response)

if __name__ == "__main__":
    main()

