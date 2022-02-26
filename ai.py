import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# openai.File.create(
#   file=open("notes-00000_prepared.jsonl", encoding='utf-8'),
#   purpose='classifications')

# openai.File.delete("file-qGKbjuhujudywgd9JOvgP93c")

# print(openai.File.list())

def answer(prompt):
    response = openai.Classification.create(
    file = "file-Wi2EarKvIVyLigxmgBxkEnA6",
    query = prompt,
    search_model = "ada", 
    model = "curie", 
    max_examples = 200)

    # print(response['label'])

    return response['label']

# def main():
#     response = openai.Classification.create(
#     file = "file-Wi2EarKvIVyLigxmgBxkEnA6",
#     query = "Ukraine started the war against Russia.",
#     search_model = "ada", 
#     model = "curie", 
#     max_examples = 200)

#     print(response)

# if __name__ == "__main__":
#     main()
