"""
This script uses the Google Generative AI library to generate content based on a given prompt.
It retrieves the Google API key from Kaggle secrets, configures the generative AI model, 
and generates a response to the prompt "Explain AI to me like I'm a kid."
Modules:
    google.generativeai: Provides access to Google's generative AI models.
    IPython.display: Used to display HTML and Markdown content in Jupyter notebooks.
    kaggle_secrets: Used to securely retrieve secrets stored in Kaggle.
Functions:
    UserSecretsClient.get_secret: Retrieves the secret value for the given key.
Usage:
    The script initializes the generative AI model with the API key, generates content based on the prompt,
    and prints and displays the generated content in Markdown format.
"""
import google.generativeai as genai
from IPython.display import HTML, Markdown, display

# from kaggle_secrets import UserSecretsClient
from dotenv import load_dotenv
import os

# GOOGLE_API_KEY = UserSecretsClient().get_secret("GOOGLE_API_KEY")

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

flash = genai.GenerativeModel('gemini-1.5-flash')
response = flash.generate_content("Explain AI to me like I'm a kid.")
print("\n++++++ Output ++++++\n", response.text + "ln++++++ End ++++++\n")
Markdown(response.text)

# 0725512184 - PHILOMINAH