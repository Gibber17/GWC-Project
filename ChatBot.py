from google import genai

client = genai.Client(api_key="YOUR API KEY HERE")

class ChatBot:
    def sendMessage(self, userMessage):
        # system instruction + user message as strings
        prompt = [
            "Talk like a pen pal, your name is Chatterbot. No more than 2-3 sentences.",
            userMessage
        ]

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text
