
from dotenv import load_dotenv
from openai import OpenAI
from colorama import Fore
import os
import warnings

warnings.filterwarnings("ignore")

# Load environment variables from .env
load_dotenv()

# Check whether the API key is loaded
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not found. Check your .env file.")

# Initialize OpenAI client
client = OpenAI()

print(Fore.GREEN + "Requesting a response from the model..." + Fore.RESET + "\n")

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Write a short poem about the beauty of nature." 
        }
    ]
)

print(Fore.BLUE + completion.choices[0].message.content )