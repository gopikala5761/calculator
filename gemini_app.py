import os
from google import genai

# Initialize the client (picks up the GEMINI_API_KEY environment variable)
client = genai.Client()

# Generate content
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='Explain how to build AI apps in 50 words.',
)

print('Gopi says:'+response.text)
