#An agent that automates tasks of creating posts on social media platforms.
#agent posting on telegram



import os
from datetime import datetime, timedelta

class Config:        #Configuration class for telegram social media posting agent
    
     # Bot Configuration
    BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', '7900111360:AAFqYQ1LaanFLh_jYj879Q2nzAIiei4LUK0')
    
      # Default Chat/Channel IDs (you can have multiple)
    DEFAULT_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID', '1433455916')

 # Scheduling Configuration
    SCHEDULER_CHECK_INTERVAL = 30  # seconds
    MAX_RETRIES = 3
    RETRY_DELAY = 60  # seconds
    
    # File Paths
    MEDIA_FOLDER = 'media/'
    LOGS_FOLDER = 'logs/'
    POSTS_BACKUP_FILE = 'scheduled_posts.json'
    
    POST_TEMPLATES = {
       'Daily Motivation': 'Here is your daily dose of motivation: {quote}',
       'Daily health tip': 'Health Tip of the Day: {tip}',
       'Daily News': 'Here are the top news headlines for today: {headlines}',
        
    }
    