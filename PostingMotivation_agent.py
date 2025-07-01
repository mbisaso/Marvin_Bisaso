import asyncio
import aiohttp
import json
import random
from datetime import datetime, time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MotivationBot:
    def __init__(self, bot_token):
        self.bot_token = bot_token
        self.base_url = f"https://api.telegram.org/bot{bot_token}"
        self.subscribers = set()
        
  # Motivational quotes database
        self.quotes = [
             "Don't let yesterday take up too much of today. - Will Rogers",
              "The way to get started is to quit talking and begin doing. - Walt Disney",
              "Believe you can and you're halfway there. - Theodore Roosevelt",
               "The only impossible journey is the one you never begin. - Tony Robbins",
               "Experience is a hard teacher because she gives the test first, the lesson afterwards. - Vernon Law"
        ]
    
    async def send_message(self, chat_id, text):
        """Send a message to a specific chat"""
        url = f"{self.base_url}/sendMessage"
        data = {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "HTML"
        }
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=data) as response:
                    result = await response.json()
                    if result.get('ok'):
                        logger.info(f"Message sent successfully to {chat_id}")
                        return result
                    else:
                        logger.error(f"Failed to send message: {result}")
                        return None
        except Exception as e:
            logger.error(f"Error sending message: {e}")
            return None
    
    async def get_updates(self, offset=None):
        """Get updates from Telegram"""
        url = f"{self.base_url}/getUpdates"
        params = {"timeout": 10}
        if offset:
            params["offset"] = offset
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, params=params) as response:
                    return await response.json()
        except Exception as e:
            logger.error(f"Error getting updates: {e}")
            return None
    
    async def handle_message(self, message):
        """Handle incoming messages"""
        chat_id = message['chat']['id']
        text = message.get('text', '').lower()
        user_name = message['from'].get('first_name', 'Friend')
        
        if text.startswith('/start'):
            self.subscribers.add(chat_id)
            welcome_msg = f"""
<b>Welcome to Daily Motivation, {user_name}!</b> 

I'll send you inspiring quotes every day to keep you motivated!

<b>Commands:</b>
/start - Subscribe to daily quotes
/stop - Unsubscribe from daily quotes
/quote - Get a random quote right now
/help - Show this help message

You're now subscribed to daily motivational quotes! 
            """
            await self.send_message(chat_id, welcome_msg)
            
        elif text.startswith('/stop'):
            if chat_id in self.subscribers:
                self.subscribers.remove(chat_id)
                await self.send_message(chat_id, " You've unsubscribed from daily quotes. Use /start to subscribe again!")
            else:
                await self.send_message(chat_id, "You weren't subscribed to daily quotes. Use /start to subscribe!")
                
        elif text.startswith('/quote'):
            quote = random.choice(self.quotes)
            formatted_quote = f" <b>Your Motivation for Today:</b>\n\n<i>\"{quote}\"</i>\n\n Keep pushing forward!"
            await self.send_message(chat_id, formatted_quote)
            
        elif text.startswith('/help'):
            help_msg = """
     <b>Daily Motivation Bot Help</b>

<b>Commands:</b>
/start - Subscribe to daily quotes
/stop - Unsubscribe from daily quotes  
/quote - Get a random quote right now
/help - Show this help message

<b>About:</b>
I send motivational quotes every day at 8:00 AM to help you start your day with positivity! 
            """
            await self.send_message(chat_id, help_msg)
            
        else:
            # Respond to any other message
            quote = random.choice(self.quotes)
            response = f"Hello {user_name}! \n\nHere's a motivational quote for you:\n\n <i>\"{quote}\"</i>\n\nUse /help to see all commands!"
            await self.send_message(chat_id, response)
            
    async def send_daily_quotes(self):
        """Send daily quotes to all subscribers"""
        if not self.subscribers:
            logger.info("No subscribers for daily quotes")
            return
        
        quote = random.choice(self.quotes)
        current_date = datetime.now().strftime("%B %d, %Y")
        
        daily_message = f"""
<b>Good Morning! Daily Motivation - {current_date}</b>

 <i>"{quote}"</i>

 Have an amazing day ahead! Remember, every day is a new opportunity to grow and achieve your dreams.

<i>Use /quote for more inspiration anytime!</i>
        """
        
        successful_sends = 0
        failed_sends = 0
        
        for chat_id in self.subscribers.copy():  # Use copy to avoid modification during iteration
            result = await self.send_message(chat_id, daily_message)
            if result:
                successful_sends += 1
            else:
                failed_sends += 1
                # Remove subscriber if bot was blocked
                if result is None:
                    self.subscribers.discard(chat_id)
                    logger.info(f"Removed blocked user: {chat_id}")
        
        logger.info(f"Daily quotes sent - Success: {successful_sends}, Failed: {failed_sends}")
        
    async def schedule_daily_quotes(self):
        """Schedule daily quotes to be sent at 8:00 AM"""
        while True:
            now = datetime.now()
            # Set target time to 8:00 AM
            target_time = now.replace(hour=8, minute=0, second=0, microsecond=0)
            
            # If it's already past 8 AM today, schedule for tomorrow
            if now >= target_time:
                target_time = target_time.replace(day=target_time.day + 1)
            
            # Calculate seconds until target time
            seconds_until_target = (target_time - now).total_seconds()
            
            logger.info(f"Next daily quote scheduled for: {target_time}")
            
            # Wait until target time
            await asyncio.sleep(seconds_until_target)
            
            # Send daily quotes
            await self.send_daily_quotes()
            
            # Wait 24 hours before next cycle
            await asyncio.sleep(86400)  # 24 hours in seconds
    
    async def run(self):
        """Main bot loop"""
        logger.info("Starting Motivation Bot...")
        
        # Start the daily quotes scheduler
        daily_task = asyncio.create_task(self.schedule_daily_quotes())
        
        # Start polling for messages
        offset = None
        
        try:
            while True:
                updates = await self.get_updates(offset)
                
                if updates and updates.get('ok'):
                    for update in updates['result']:
                        offset = update['update_id'] + 1
                        
                        if 'message' in update:
                            await self.handle_message(update['message'])
                
                await asyncio.sleep(1)  # Small delay to prevent hammering the API
                
        except KeyboardInterrupt:
            logger.info("Bot stopped by user")
        except Exception as e:
            logger.error(f"Bot error: {e}")
        finally:
            daily_task.cancel()

# Usage
async def main():
    # Replace with your actual bot token
    BOT_TOKEN = "7900111360:AAFqYQ1LaanFLh_jYj879Q2nzAIiei4LUK0"
    
    bot = MotivationBot(BOT_TOKEN)
    await bot.run()

if __name__ == "__main__":
    asyncio.run(main())