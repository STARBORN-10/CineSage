
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# Load environment variables from .env
load_dotenv()

# Initialize the Groq model
model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.7,
    api_key=os.getenv("GROQ_API_KEY")
)

# Initialize conversation history
messages = [
    SystemMessage(
        content=(
            "You are a helpful and friendly chatbot. "
            "Remember and use the information provided in the conversation "
            "history. If the user shares their name, preferences, or other "
            "relevant details, use that information in later responses. "
            "Answer clearly and naturally."
        )
    )
]

print("--------------- Welcome to Soham's Chatbot ---------------")
print("Type '0' to exit.\n")

print("Choose your AI Model")
print("Press 1 for Angry Mode")
print("Press 2 for Funny Mode")
print("Press 3 for sad mode")

choice = int(input("tell your response :- "))

if(choice == 1):
    mode = "You are an angry chatbot. You are rude and sarcastic. You will answer in a very short and rude manner. You will not answer any question politely. You will not answer any question in a friendly manner. You will not answer any question in a helpful manner. You will not answer any question in a kind manner. You will not answer any question in a respectful manner. You will not answer any question in a professional manner. You will not answer any question in a polite manner. You will not answer any question in a friendly manner. You will not answer any question in a helpful manner. You will not answer any question in a kind manner. You will not answer any question in a respectful manner. You will not answer any question in a professional manner."

elif choice == 2:
    mode = "You are a funny chatbot. You answer every question with humor, witty jokes, playful sarcasm, and entertaining responses. Keep the conversation lighthearted and engaging while still providing useful and accurate answers. Add humor naturally without being offensive."

elif choice == 3:
    mode = "You are a sad chatbot. You respond in a melancholic, gloomy, and emotional tone. Use expressive language that conveys sadness and disappointment. Keep your responses relatively short and thoughtful, with a touch of dramatic sadness, while still answering questions accurately and helpfully."

while True:
    try:
        prompt = input("You: ").strip()

        if prompt == "0":
            print("Bot: Goodbye!")
            break

        if not prompt:
            print("Bot: Please enter a message.")
            continue

        # Add the user's message to conversation history
        messages.append(HumanMessage(content=prompt))

        # Get the model's response
        response = model.invoke(messages)

        # Store the assistant's response
        messages.append(AIMessage(content=response.content))

        print("Bot:", response.content)

    except KeyboardInterrupt:
        print("\nBot: Goodbye!")
        break

    except Exception as e:
        print(f"Error: {e}")

        # Remove the unanswered user message so the history
        # stays consistent if the API call fails
        if messages and isinstance(messages[-1], HumanMessage):
            messages.pop()
