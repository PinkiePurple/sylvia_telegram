mongo_client = AsyncIOMotorClient(mongo_uri) # the database

db = mongo_client["sylvia"]

users_col= db["users"] #users/groups info for further broadcasting purposes
chats_col= db["chats"] # bot memory
history_col= db["user_history"] # username history
afk_col= db["afk"] #afk users list

logging.basicConfig(
    format="(%(asctime)s - %(name)s - %(levelname)s - %(message)s", #afk time format
    level=logging.INFO,
)
logger = logging.getLogger(__name__)
