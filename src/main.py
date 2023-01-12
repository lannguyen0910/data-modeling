from loguru import logger

from database import main as database_main
from etl import main as etl_main

# Configure logger
logger.add("logs/info.log", rotation="1 MB", retention="10 days", level="INFO")
logger.add("logs/debug.log", rotation="1 MB",
           retention="10 days", level="DEBUG")

if __name__ == "__main__":
    database_main()
    etl_main()
