import asyncio
import os
import json
import logging
import random
import tempfile
import urllib.parse
import aiohttp
import re

from uuid import uuid4
from datetime import (
    datetime,
    timezone,
)

from collections import (
    defaultdict,
    deque,
)

from telegram import (
    Update,
    Bot,
    Message,
    Chat,
    User,
)

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackContext,
    ContextTypes,
    callbackqueryhandler,
)

from telegram.constants import chataction
from telegram.error import (
    TelegramError,
    BadRequest,
    Unauthorized,
)

from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
