import logging
from logging.config import dictConfig

logging_config = dict(
    version=1,
    formatters={
        'f': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s : %(threadName)s'
        }
    },
    handlers={
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'f',
            'level': logging.DEBUG
        },
        'file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'f',
            'when': 'midnight',
            'filename': './logs/app.log',
            'backupCount': 5
        }
    },
    root={
        'handlers': ['console', 'file'],
        'level': logging.DEBUG
    },
    disable_existing_loggers=False
)

dictConfig(logging_config)
