LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console_formatter': {
            'format': "{message}",
            'style': "{"
        },
        'file_formatter': {
            'format': "{levelname} {asctime} \n\tModule: {module} \n\tFile: {filename} \n\tLine No: {lineno} \n\tMessage: {message}",
            'style': "{"
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            "level": "DEBUG",
            "formatter": "console_formatter"
        },
        'file': {
            'class': 'logging.FileHandler',
            'level': 'INFO',
            'filename': 'logs/stable_candybit_social.log',
            'formatter': "file_formatter",
            'encoding': 'utf-8',
            "mode":"a"
        },
    },

    'loggers': {
        'django': {
            'handlers': ["file", "console"],
            'level': "INFO",
            'propagate': False,
        },
    }
}