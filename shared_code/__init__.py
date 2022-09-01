import datetime
import logging
import azure.durable_functions as df

CACHED_TIME = None

class Config:
    def load(self):
        logging.info(">>> Loading config...")
        global CACHED_TIME
        if CACHED_TIME is None:
            logging.info(">>> Config not cached, setting new value...")
            CACHED_TIME = datetime.datetime.utcnow().isoformat()
        else:
            logging.info(">>> Using cached value...")
        
        logging.info(f">>> Returning value {CACHED_TIME}")
        return CACHED_TIME

class Logger:
    def __init__(self, context: df.DurableOrchestrationContext):
        self.context = context
    
    def log(self, message: str):
        if not self.context.is_replaying:
            logging.info(message)

    def info(self, message: str):
        if not self.context.is_replaying:
            logging.info(message)
    
    def debug(self, message: str):
        if not self.context.is_replaying:
            logging.debug(message)
    
    def warning(self, message: str):
        if not self.context.is_replaying:
            logging.warning(message)

    def error(self, message: str):
        if not self.context.is_replaying:
            logging.error(message)
    
    def critical(self, message: str):
        if not self.context.is_replaying:
            logging.critical(message)
    
    def exception(self, message: str):
        if not self.context.is_replaying:
            logging.exception(message)
