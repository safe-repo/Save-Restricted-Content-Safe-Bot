#Safe_repo

import logging
import time
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)
import pyrogram.utils
pyrogram.utils.MIN_CHANNEL_ID = -1009999999999

botStartTime = time.time()

if __name__ == "__main__":
    from . import bot
    import glob
    from pathlib import Path
    from Safe_repo.importer import load_plugins
    
    path = "Safe_repo/assets/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem
            load_plugins(plugin_name.replace(".py", ""))

    logger.info("Bot Started :)")

    
    bot.run_until_disconnected()
