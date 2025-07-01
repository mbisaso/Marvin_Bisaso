import asyncio
import aiohttp

async def test_telegram_connection():
    BOT_TOKEN = "7900111360:AAFqYQ1LaanFLh_jYj879Q2nzAIiei4LUK0"  
    CHAT_ID = "1433455916"    
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    
    data = {
        "chat_id": CHAT_ID,
        "text": " Success! Your Telegram bot is working perfectly!"
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data) as response:
            result = await response.json()
            
            if result.get('ok'):
                print("Test message sent successfully!")
                print(f"Message ID: {result['result']['message_id']}")
            else:
                print(f" Error: {result}")

# Run the test
asyncio.run(test_telegram_connection())