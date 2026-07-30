import imports

load_dotenv()

telegram_token = os.getenv("TELEGRAM_TOKEN")
groq_api_key = os.getenv("GROQ_API_KEY")
render_url= os.getenv("RENDER_URL")
mongo_uri = os.getenv("MONGO_URI")

