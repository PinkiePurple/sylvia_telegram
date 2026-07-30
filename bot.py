MEMORY_SIZE = 20

BOT_USERNAME: str | None = None
BOT_USER_ID: int | None = None

user_memory: dict[int, deque] = defaultdict(lambda: deque(maxlen=MEMORY_SIZE))

BASE_SYSTEM_PROMPT = (...)
