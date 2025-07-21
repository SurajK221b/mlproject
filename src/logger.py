import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


### TO TEST THE LOGGER ###
# Uncomment the following lines to test the logger
# if __name__ == "__main__":
#     logging.info("Logger is configured and ready to use.")
#     logging.error("This is a test error message.")
#     logging.warning("This is a test warning message.")
#     logging.debug("This is a test debug message.")
#     logging.critical("This is a test critical message.")