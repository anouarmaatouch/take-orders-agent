import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Vonage
    VONAGE_API_KEY = os.environ.get('VONAGE_API_KEY')
    VONAGE_API_SECRET = os.environ.get('VONAGE_API_SECRET')
    VONAGE_APPLICATION_ID = os.environ.get('VONAGE_APPLICATION_ID')
    VONAGE_PRIVATE_KEY_PATH = os.environ.get('VONAGE_PRIVATE_KEY_PATH')
    
    # OpenAI
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
    
    # Server
    PUBLIC_URL = os.environ.get('PUBLIC_URL')
