"""EduQuest - Configuration"""
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'eduquest-secret-key-change-in-prod')
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///eduquest.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'jwt-secret-key-change-in-prod')
    OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY', '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')
