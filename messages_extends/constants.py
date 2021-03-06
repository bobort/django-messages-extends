# -*- coding: utf-8 -*-
"""constants.py: messages extends"""


DEBUG = 10
INFO = 20
SUCCESS = 25
WARNING = 30
ERROR = 40

DEBUG_PERSISTENT = 11
INFO_PERSISTENT = 21
SUCCESS_PERSISTENT = 26
WARNING_PERSISTENT = 31
ERROR_PERSISTENT = 41

DEBUG_STICKY = 12
INFO_STICKY = 22
SUCCESS_STICKY = 27
WARNING_STICKY = 32
ERROR_STICKY = 42

DEFAULT_TAGS = {
    DEBUG_PERSISTENT: 'debug persistent',
    INFO_PERSISTENT: 'info persistent',
    SUCCESS_PERSISTENT: 'success persistent',
    WARNING_PERSISTENT: 'warning persistent',
    ERROR_PERSISTENT: 'error persistent',

    DEBUG_STICKY: 'debug sticky',
    INFO_STICKY: 'info sticky',
    SUCCESS_STICKY: 'success sticky',
    WARNING_STICKY: 'warning sticky',
    ERROR_STICKY: 'error sticky',

}

PERSISTENT_MESSAGE_LEVELS = (
    DEBUG_PERSISTENT, INFO_PERSISTENT, SUCCESS_PERSISTENT, WARNING_PERSISTENT, ERROR_PERSISTENT
)
STICKY_MESSAGE_LEVELS = (
    DEBUG_STICKY, INFO_STICKY, SUCCESS_STICKY, WARNING_STICKY, ERROR_STICKY
)
