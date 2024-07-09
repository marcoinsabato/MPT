import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration for database connection
DATABASE_CONFIG = {
    'dbtype' : os.getenv('DB_TYPE'),
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT')
}

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')