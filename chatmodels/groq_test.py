from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

model = init_chat_model("groq:openai/gpt-oss-120b")

response = model.invoke("Who is Chhatrapati Shivaji Maharaj?")
print(response.content)