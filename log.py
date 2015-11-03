import logging
import datetime

timenow = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")

def login(usr, message):
    LOG_FILENAME = 'log.out'

    handler = ''

    FORMAT = "%(message)s"
    logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.DEBUG,
                    format=FORMAT
                    )

    d = {'user': usr}
    logging.info(timenow + " | User: " + usr + " Result: " + message)

    logging.debug('')

    f = open(LOG_FILENAME, 'rt')

    f.close()

def error(e):
    LOG_FILENAME = 'log.out'
    
    FORMAT = "%(message)s"
    logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.DEBUG,
                    format=FORMAT
                    )
    
    logging.error(timenow + " | Error: " + e)

    f = open(LOG_FILENAME, 'rt')
  
    f.close()
