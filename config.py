import os
from dotenv import load_dotenv
from redis_dict import RedisDict

load_dotenv('.env')
TOKEN = os.getenv('BOT_TOKEN')
db = RedisDict('books')
print(db)

