from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import configurebot

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

storage=MemoryStorage()
bot = Bot(token=configurebot.cfg['token'])
dp = Dispatcher(bot, storage=storage)