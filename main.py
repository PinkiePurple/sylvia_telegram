import imports
import bot
import mongo
import definitions

load_dotenv()

telegram_token = os.getenv("TELEGRAM_TOKEN")
groq_api_key = os.getenv("GROQ_API_KEY")
render_url= os.getenv("RENDER_URL")
mongo_uri = os.getenv("MONGO_URI")

groq_chat_url = "https://api.groq.com/v1/chat/completions"
groq_whisper_url = "https://api.groq.com/v1/audio/transcriptions"

groq_models = [
    "llama-3.3-70b-versatile",
    "llama-3.1-80b-instant",
    "gemma-2-9b-it",
]

klipy_api_key = os.getenv("KLIPY_API_KEY")
