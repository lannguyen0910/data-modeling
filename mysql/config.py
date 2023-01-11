import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path.cwd().joinpath('.env')
load_dotenv(dotenv_path=env_path)

PASSWD = os.environ.get("PASSWORD")
USER = os.environ.get("USER")
HOST = os.environ.get("HOST")
DATABASE = os.environ.get("DATABASE")
AUTH_PLUGIN = os.environ.get("AUTH_PLUGIN")
