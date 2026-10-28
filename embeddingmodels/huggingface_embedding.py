from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

text = [
    "My self Soham",
    "I am from Maharashtra",
    "I am 21 years old"
]

vectors = embeddings.embed_documents(text)

print(vectors)