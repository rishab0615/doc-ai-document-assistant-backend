from google import genai
from app.config import GEMINI_API_KEY
from google.genai import types


client = genai.Client(api_key=GEMINI_API_KEY)


def generate_embedding(text: str):
    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text,
        config=types.EmbedContentConfig(
            output_dimensionality=768,
        ),
    )
    return response.embeddings[0].values  ##-- In our case we are sending just one single text so we need to access only the first embeddings --##