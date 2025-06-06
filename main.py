# -*- coding: utf-8 -*-

from pathlib import Path # 引入Path类是为了适配不同系统的路径分隔符不同(windows\linux/)

from ncatbot.utils.config import config
from ncatbot.core.client import BotClient
from ncatbot.core.message import GroupMessage, PrivateMessage
from ncatbot.utils.logger import get_log

config_yaml_path = str(Path("config.yaml"))
config.load_config(config_yaml_path) # 从文件加载配置, 一定版本后的ncatbot会自动完成这一步
bot = BotClient() # 创建BotClient
logger = get_log() # 创建logger

@bot.group_event()
async def on_group_message(msg: GroupMessage):
    pass

@bot.private_event()
async def on_private_message(msg: PrivateMessage):
    logger.info(msg)

if __name__ == "__main__":
    bot.run()