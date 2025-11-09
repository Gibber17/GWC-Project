from google import genai

client = genai.Client(api_key="AIzaSyAmegGOYvBn_jsnrZjW6OAdENgt-j1qQ-A")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="In one short paragraph. Explain how AI works in a few words"
)
print(response.text)