"""
    Author: Ethan Zavaglia
    Purpose: Log various data
    Course: IST 440W
    Date: 11/3/2015
    Revision: 2
"""

import logging
import datetime

timenow = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")

def login(module, usr, message):
    LOG_FILENAME = 'audit.out'

    handler = ''

    FORMAT = "%(message)s"
    logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.DEBUG,
                    format=FORMAT
                    )

    d = {'user': usr}
    logging.info(timenow + " | Module: " + module + " User: " + usr + " Result: " + message)

    logging.debug('')

    f = open(LOG_FILENAME, 'rt')

    f.close()

def error(e):
    LOG_FILENAME = 'error.out'
    
    FORMAT = "%(message)s"
    logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.DEBUG,
                    format=FORMAT
                    )
    
    logging.error(timenow + " | Error: " + type(e).__name__)

    f = open(LOG_FILENAME, 'rt')
  
    f.close()
