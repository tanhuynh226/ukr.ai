import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

fileID = openai.File.create(
  file=open("patricktrain_prepared.jsonl", encoding='utf-8'),
  purpose='classifications')

print(fileID['id'])

# openai.File.delete("file-30S3eZx2cjWP4zlvpUonSAG7")