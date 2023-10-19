from beanie import init_beanie
import motor.motor_asyncio
from server.models.question import Question, StaarQuestion, MathworldQuestion, CollegeQuestion, Activity
from server.models.account import Account, SubscriberAccount
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_DETAILS = os.getenv('MONGO_DETAILS')
DB_NAME = os.getenv('DB_NAME')
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
db = client[DB_NAME]

async def init_db():
    await init_beanie(database=client[DB_NAME],
                      document_models=[Question, StaarQuestion, MathworldQuestion, CollegeQuestion,
                                    Account, SubscriberAccount, Activity])