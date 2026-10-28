
import os
from dotenv import load_dotenv
from typing import List, Optional

from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")


# Define the Movie structure
class Movie(BaseModel):
    title: str
    release_year: Optional[int] = None
    genre: List[str] = Field(default_factory=list)
    director: Optional[str] = None
    cast: List[str] = Field(default_factory=list)
    rating: Optional[float] = None
    summary: str = ""


# Initialize the output parser
parser = PydanticOutputParser(pydantic_object=Movie)


# Initialize the Groq model
model = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=api_key,
    temperature=0.7
)


# Create the prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a professional Movie Information Extraction Assistant.

            Extract movie information from the given paragraph.
            Use only information provided in the paragraph.
            Do not invent missing details.

            {format_instructions}
            """
        ),
        ("human", "{paragraph}")
    ]
)


# Run only when core.py is executed directly
if __name__ == "__main__":
    para = input("Give your paragraph: ")

    final_prompt = prompt.invoke({
        "paragraph": para,
        "format_instructions": parser.get_format_instructions()
    })

    response = model.invoke(final_prompt)

    movie_data = parser.parse(response.content)

    print(movie_data.model_dump_json(indent=2))
