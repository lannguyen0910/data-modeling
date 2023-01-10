import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path.cwd().joinpath('.env')
load_dotenv(dotenv_path=env_path)

PASSWD = os.environ.get("PASSWORD")
USER = os.environ.get("USER", "root")
HOST = os.environ.get("HOST", "localhost")
DATABASE = os.environ.get("DATABASE", "sparkifydb")
AUTH_PLUGIN = os.environ.get("AUTH_PLUGIN", "mysql_native_password")
