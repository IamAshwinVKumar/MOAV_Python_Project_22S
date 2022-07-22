""" Used for recording events in a Log file """
# To be noted that this is to demonstrate the working of log files,it is not actually associated with our 'main.py'
from config import logging

# The location of Log file is defined here
log_file = "./log_records.log"

# Logging configuration
logging.basicConfig(filename=log_file, filemode="w", format="%(name)s - %(asctime)s - %(message)s", level=logging.DEBUG)
logging.warning('This activity will be logged to the Log file')
logging.getLogger().addHandler(logging.StreamHandler())

# to handle error exceptions from matplotlib
logging.getLogger('matplotlib.font_manager').disabled = True

# Ending logging
logging.shutdown()
