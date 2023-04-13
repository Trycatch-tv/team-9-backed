import os
from dotenv import load_dotenv
from pathlib import Path


# ============================================================
# Configuration .evn WAROCOL.COM
# ============================================================

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:

    PROJECT_NAME:str = "Team 9 RESERVATION TABLES RESTAURANT"
    PROJECT_VERSION:str = "1.0"
    USR_MONGO_DB:str = os.getenv('USR_MONGO_DB')
    PASS_MONGO_DB:str = os.getenv('PASS_MONGO_DB')
    CLUSTER_MONGO_DB:str = os.getenv('CLUSTER_MONGO_DB')
    URL_CLUSTER_MONGO_DB = f"mongodb+srv://{USR_MONGO_DB}:{PASS_MONGO_DB}@{CLUSTER_MONGO_DB}.uho1qgv.mongodb.net/test"


settings = Settings()