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
    file = "file-R5VA59nOEqhU4L0QgR3EyGTK",
    query = prompt,
    search_model = "curie", 
    model = "curie", 
    labels = ["NOT_MISLEADING", "MISINFORMED_OR_POTENTIALLY_MISLEADING"],
    max_examples = 200)

    # print(response['label'])

    return response['label']

# nobirdwatch training : file-5tWsG9oQZyrIW5JGt6YvKas3
# birdwatch + manual training : file-R5VA59nOEqhU4L0QgR3EyGTK

def main():
    response = openai.Classification.create(
    file = "file-i5K6dpIvAcYzNDDUW60bX6Kn",
    query = "Russia started the conflict with Ukraine.",
    search_model = "curie", 
    model = "curie", 
    labels = ["NOT_MISLEADING", "MISINFORMED_OR_POTENTIALLY_MISLEADING"],
    max_examples = 1000)
    
    print(response['label'])

if __name__ == "__main__":
    main()

