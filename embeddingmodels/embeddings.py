from dotenv import load_dotenv
from langchain_openai import OpenaiEmbeddings

load_dotenv()

embeddings = OpenaiEmbeddings(
    model = "text-embedding-3-large",
    dimensions = 64
)

vector = embeddings.embed_query("You are going to learn genAI ")

print(vactor)

