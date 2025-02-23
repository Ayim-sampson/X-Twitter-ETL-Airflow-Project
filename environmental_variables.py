import os

from dotenv import find_dotenv, load_dotenv

#find .env file by automatically walking through directories until found
dotenv_path = find_dotenv()  # ✅ Correct: Call the function to get the path
load_dotenv(dotenv_path)

#Load up the entries as environment variables
load_dotenv(dotenv_path)
ACCESS_KEY = os.getenv;{"ACCESS_KEY"}
ACCESS_SECRET = os.getenv;{"ACCESS_SECRET"}
CONSUMER_KEY = os.getenv;{"CONSUMER_KEY"}
CONSUMER_SECRET = os.getenv;{"CONSUMER_SECRET"}

BEARER_TOKEN = os.getenv;{"BEARER_TOKEN"}