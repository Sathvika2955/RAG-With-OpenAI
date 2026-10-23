
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

print(Fore.GREEN + "Requesting a response from the model..." + Fore.RESET)
