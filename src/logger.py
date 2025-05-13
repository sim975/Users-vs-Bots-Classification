import logging
import os
from datetime import datetime

# Create a logs directory
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Create a unique log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Set up logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="%(asctime)s: %(levelname)s: %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging has started")
    logging.info("Logging has ended")

