# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX


class Config(object):
    # Configuration class for the bot

    # Enable or disable logging
    LOGGER = True

    # <================================================ REQUIRED ======================================================>
    # Telegram API configuration
    API_ID = 24658337  # Get this value from my.telegram.org/apps
    API_HASH = "bf99242dbb7f3501f28d39f0a0383cbf"

    # Database configuration (PostgreSQL)
    DATABASE_URL = "postgres://ljdriyar:QpkDtjVV2bMteyGZar7-lT0ebd660Acm@lucky.db.elephantsql.com/ljdriyar"

    # Event logs chat ID and message dump chat ID
    EVENT_LOGS = -1001982513585
    MESSAGE_DUMP = -1001982513585

    # MongoDB configuration
    MONGO_DB_URI = "mongodb+srv://Itachi:Itachi@itachi.rcfnknv.mongodb.net/?retryWrites=true&w=majority"

    # Support chat and support ID
    SUPPORT_CHAT = "Devine_Support"
    SUPPORT_ID = -1001982513585

    # Database name
    DB_NAME = "MikoDB"

    # Bot token
    TOKEN = "6924632975:AAG96JkzNKBIgRb1yxP06ZqPSBRu2JyCHfI"  # Get bot token from @BotFather on Telegram

    # Owner's Telegram user ID (Must be an integer)
    OWNER_ID = 6402009857
    # <=======================================================================================================>

    # <================================================ OPTIONAL ======================================================>
    # Optional configuration fields

    # List of groups to blacklist
    BL_CHATS = []

    # User IDs of sudo users, dev users, support users, tiger users, and whitelist users
    DRAGONS = [6440363814]  # Sudo users
    DEV_USERS = []  # Dev users
    DEMONS = []  # Support users
    TIGERS = []  # Tiger users
    WOLVES = []  # Whitelist users

    # Toggle features
    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True

    # Modules to load or exclude
    LOAD = []
    NO_LOAD = []

    # Global ban settings
    STRICT_GBAN = True

    # Temporary download directory
    TEMP_DOWNLOAD_DIRECTORY = "./"
    # <=======================================================================================================>


# <=======================================================================================================>


class Production(Config):
    # Production configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True


class Development(Config):
    # Development configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True
