import logging
from datetime import datetime

from project.config import LOG_PATH

logger = logging.getLogger('project')
syslog = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s', datefmt='%H:%M:%S')
syslog.setFormatter(formatter)
logger.setLevel(logging.INFO)
logger.addHandler(syslog)

log_file_name = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
log_file_path = f'{LOG_PATH}/{log_file_name}.log'
logger.info(f'Logging to file: "{log_file_path}"')
open(log_file_path, 'w').close()

file_handler = logging.FileHandler(log_file_path)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.info('Finished setting up logging!')
