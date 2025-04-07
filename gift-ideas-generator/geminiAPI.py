import os
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel
from deep_translator import GoogleTranslator


class GiftIdea(BaseModel):
    gift_name: str
    description: str
    price_range: str


class GeminiAPI:
    def __init__(self, language="polish", ideasCount=5):
        load_dotenv()
        self.api_key = os.getenv("GEMINI_API_KEY")

        if not self.api_key:
            raise ValueError(
                "API key not found! Set GEMINI_API_KEY in environment variables.")

        self.client = genai.Client(api_key=self.api_key)
        self.gift_ideas = []
        self.language = language
        self.ideasCount = ideasCount
        self.stored_data = {}
        self.translator = GoogleTranslator(source=self.language, target="en")

    def formatToLanguage(self):
        """Translate stored data to English."""
        for key, value in self.stored_data.items():
            if key == 'age' or key == 'max_budget':
                continue
            elif isinstance(value, list):
                self.stored_data[key] = [
                    self.translator.translate(item) for item in value]
            else:
                self.stored_data[key] = self.translator.translate(value)

    def gen_gift_ideas(self, stored_data: dict) -> str:
        """Generate gift ideas based on user input."""
        self.stored_data = stored_data
        self.formatToLanguage()

        contents = (
            f"Suggest {self.ideasCount} gifts for a {stored_data['age']}-year-old {stored_data['sex']} "
            f"who is my {stored_data['relationship']}. My budget is {stored_data['max_budget']}. "
            f"{stored_data['relationship'].capitalize()} likes {', '.join(stored_data['hobbies'])}. "
            f"The occasion is {stored_data['celebration']}. "
            f"Please answer in {self.language}.")

        print(contents)
        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=contents,
            config={
                'response_mime_type': 'application/json',
                'response_schema': list[GiftIdea],
            },
        )

        self.gift_ideas = response.parsed

    def get_gift_ideas(self) -> str:
        """Get generated gift ideas."""
        examples = []
        for idx, idea in enumerate(self.gift_ideas):
            examples.append(
                f"{idx+1}. {idea.gift_name}\n* {idea.description}\n* {idea.price_range}\n\n")

        return examples
