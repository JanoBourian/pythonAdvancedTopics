import logging 
import os
root = os.path.join(os.path.abspath(os.path.dirname(__file__)), "example.log")

logging.basicConfig(filename=root, filemode="a", encoding='utf-8', format = '%(levelname)s:%(asctime)s %(message)s', level=logging.DEBUG, force=True)
logger = logging.getLogger(__name__)
logger.info("Maybe you can see me")
logger.warning("Of course you can see me")
logger.debug('This message should go to the log file')
logger.info('So should this')
logger.warning('And this, too')
logger.error('And non-ASCII stuff, too, like Øresund and Malmö')