
from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model
model = init_chat_model("groq:openai/gpt-oss-120b" , temperature=0.5 , max_tokens=20)

response = model.invoke("What is Maharashtra ?")
print(response.content)
