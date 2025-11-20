from google import genai

client = genai.Client(api_key="AIzaSyAmegGOYvBn_jsnrZjW6OAdENgt-j1qQ-A")

class ChatBot:
    def sendMessage(self, userMessage):
        # system instruction + user message as strings
        prompt = [
            "No sentence longer than 8–10 words. Talk like a pen pal.",
            userMessage
        ]

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text
