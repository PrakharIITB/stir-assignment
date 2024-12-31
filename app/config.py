import os
from dotenv import load_dotenv

load_dotenv(override=True)

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'defaultsecretkey')
    MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/')
    DB_NAME = os.getenv('DB_NAME', 'stir')
    COLLECTION_NAME = 'stir'
    PROXY_USERNAME = os.getenv('PROXY_USERNAME')
    PROXY_PASSWORD = os.getenv('PROXY_PASSWORD')
    PROXY_HOST = os.getenv('PROXY_HOST')
    PROXY_PORT = os.getenv('PROXY_PORT')
    TWITTER_USERNAME = os.getenv('TWITTER_USERNAME')
    TWITTER_PASSWORD = os.getenv('TWITTER_PASSWORD')
    TWITTER_EMAIL = os.getenv('TWITTER_EMAIL')