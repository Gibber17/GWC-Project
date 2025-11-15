from google import genai

client = genai.Client(api_key="AIzaSyAmegGOYvBn_jsnrZjW6OAdENgt-j1qQ-A")

class ChatBot:
    def sendMessage(userMessage):
        response = client.models.generate_content(
            model="gemini-2.5-flash", contents=userMessage
        )
        print(response.text)
