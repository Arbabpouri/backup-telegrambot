import datetime
import os
from telethon import TelegramClient
from telethon.tl.types import PeerUser
import asyncio


config = {
    "apiID": 123,
    "apiHash": "",
    "botToken": "",
    "directorys": [r"./log.txt"], 
    "adminsUserIds": [2056493966],
}


async def main() -> None:

    client = TelegramClient(
        session="bot",
        api_id=config["apiID"],
        api_hash=config["apiHash"]
    )
    
    await client.start(bot_token=config["botToken"]) 
        
    try:
        
        for user in config.get('adminUserId', []):
            
            time = datetime.datetime.now()
            await client.send_message(PeerUser(user), f"BackUp in {time} 👇👇👇")
            
            for file in config.get('directorys', []):
                
                if not os.path.exists(file):
                    continue
                
                try:
                    await client.send_file(PeerUser(user), file, caption=f'BackUp for {file}')
                    print(f"{file} sent to {user} successfully.")
                except Exception as e:
                    print(f'error in send, file = {file} and user {user}, error:', e)
            
            

    except Exception as ex:
        print(f"An error occurred: {ex}")
    finally:
        await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
