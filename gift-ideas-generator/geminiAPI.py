import os
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel


class GiftIdea(BaseModel):
    gift_name: str
    description: str
    price_range: str


class GeminiAPI:
    def __init__(self, language="polish", ideasCount=5):
        load_dotenv()
        self.api_key = os.getenv("GEMINI_API_KEY")

        if not self.api_key:
            raise ValueError("API key not found! Set GEMINI_API_KEY in environment variables.")
        
        self.client = genai.Client(api_key=self.api_key)
        self.gift_ideas = []
        self.language = language
        self.ideasCount = ideasCount


    def gen_gift_ideas(self, stored_data : dict) -> str:
        contents = f"Suggest {self.ideasCount} gifts for a {stored_data['age']}-year-old {stored_data['sex']}         \
                    who is my {stored_data['relationship']}. My budget is {stored_data['max_budget']}.                \
                    They like {stored_data['hobbies']}. The occasion is {stored_data['celebration']}.                 \
                    Please answer in {self.language}."

        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=contents,
            config={
                'response_mime_type': 'application/json',
                'response_schema': list[GiftIdea],
            },
        )

        self.gift_ideas = response.parsed
        
    def get_gift_ideas(self):
        examples = []
        for idx, idea in enumerate(self.gift_ideas):
            examples.append(f"{idx+1}. {idea.gift_name}\n* {idea.description}\n* {idea.price_range}\n\n")

        return examples
