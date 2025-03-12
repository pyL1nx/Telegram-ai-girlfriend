# config.py
import os

class Config:
    TELEGRAM_TOKEN = 'Your Telegram Bot Token'
    GEMINI_API_KEY = 'Your Gemini API Key'
    
    # File paths
    MEMORY_FILE = 'memory.json'
    IMAGE_DIR = 'images/'
    
    # Bot personality settings
    BOT_NAME = "Yuki"
    PERSONALITY = {
        "friendliness": 0.9,
        "humor": 0.7,
        "empathy": 0.85
    }
    
    # Emotional states
    MOOD_STATES = ["happy", "sad", "excited", "bored", "affectionate"]
