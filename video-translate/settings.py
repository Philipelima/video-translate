
from dotenv import load_dotenv;
import os

load_dotenv()

ASSEMBLYAPI_KEY = os.getenv('ASSEMBLYAPI_KEY')
VIDEOS_PATH     = os.getenv('VIDEOS_PATH')

AZURE_SPEECH_SERVICE = os.getenv('AZURE_SPEECH_SERVICE_KEY')

