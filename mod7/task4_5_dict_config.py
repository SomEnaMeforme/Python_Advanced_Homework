import sys
import logging.handlers
from mod7.task3_log_handler import LogHandlerForCalculator
from mod7.task7 import ASCIIFilter

dict_config = {
    "version": 1,
    'disable_existing_loggers': True,
    "formatters": {
        "base": {
            "format": '%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s',
            "datefmt": '%Y-%m-%d %H:%M:%S',
        },
    },
    "filters": {
        "asciifilter": {
            "()": ASCIIFilter
        }
    },
    "handlers": {
        "console": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "base",
                "stream": sys.stdout,
                'filters': ["asciifilter"]
            },
        "file": {
            "()": LogHandlerForCalculator,
            "level": "DEBUG",
            "formatter": "base",
            'filters': ["asciifilter"]
            },
        "time_file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "when": 'h',
            "interval": 10,
            'backupCount': 0,
            "filename": "utils.log",
            "level": "INFO",
            'filters': ["asciifilter"]
        },
        "httpPostLogs": {
            "class": "logging.handlers.HTTPHandler",
            "host": "127.0.0.1:5000",
            "url": "/post_logs",
            "method": "POST",
            "level": "DEBUG",
        }
    },
    "loggers": {
                'CalculationLoggerApps': {
                    "level": "DEBUG",
                    "handlers": ["file", "console", "httpPostLogs"],
                    "propagate": False
                },
                'CalculationLoggerUtils': {
                    "level": "DEBUG",
                    "handlers": ["time_file", "console", "httpPostLogs"],
                    "propagate": False
                }
    }
}

