
import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Soham's AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Soham's AI Chatbot")
st.caption("Choose your AI's mood and start chatting!")

# Initialize Groq model
model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.7,
    api_key=os.getenv("GROQ_API_KEY")
)

# Available chatbot moods
modes = {
    "Angry 😡": (
        "You are an angry chatbot. You are rude and sarcastic. "
        "Answer in a short, grumpy, and sarcastic manner. "
        "Keep responses entertaining without being genuinely hurtful."
    ),
    "Funny 😂": (
        "You are a funny chatbot. Answer with humor, witty jokes, "
        "playful sarcasm, and entertaining responses. Keep the "
        "conversation lighthearted while providing accurate answers."
    ),
    "Sad 😢": (
        "You are a sad chatbot. Respond in a melancholic, gloomy, "
        "and emotional tone. Use expressive language that conveys "
        "sadness and disappointment while answering accurately."
    )
}

# Select chatbot mood
selected_mode = st.selectbox(
    "Choose your AI Model",
    list(modes.keys())
)

st.divider()

# Initialize conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display conversation history
for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)

# Chat input
prompt = st.chat_input("Type your message here...")

if prompt:
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Add user message to history
    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

    # Apply the selected mood to the system prompt
    system_message = SystemMessage(
        content=(
            "You are Soham's AI chatbot. Remember and use "
            "the conversation history. Answer clearly and naturally.\n\n"
            + modes[selected_mode]
        )
    )

    # Send conversation to the model
    conversation = [system_message] + st.session_state.messages

    try:
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = model.invoke(conversation)

            st.markdown(response.content)

        # Store assistant response
        st.session_state.messages.append(
            AIMessage(content=response.content)
        )

    except Exception as e:
        st.error(f"Error: {e}")

        # Remove unanswered user message
        if (
            st.session_state.messages
            and isinstance(st.session_state.messages[-1], HumanMessage)
        ):
            st.session_state.messages.pop()
