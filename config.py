import os
from dotenv import load_dotenv

load_dotenv('.env', verbose=True)
DATA_DIR = os.getenv('DATA_DIR')
