from langchain_google_genai import ChatGoogleGenerativeAI
from config.settings import GOOGLE_API_KEY


def crear_llm():
    """
    Crea y devuelve una instancia del modelo Gemini.
    """

    return ChatGoogleGenerativeAI(
        model="gemma-4-26b-a4b-it",
        api_key=GOOGLE_API_KEY,
        temperature=0.2,
    )