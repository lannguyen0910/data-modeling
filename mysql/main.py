from loguru import logger

from create_tables import main as create_table_main
from etl import main as etl_main

# Configure logger
logger.add("modelling.log", rotation="1 MB", retention="10 days", level="INFO")

if __name__ == "__main__":
    create_table_main()
    etl_main()
