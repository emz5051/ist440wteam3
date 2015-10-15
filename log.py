import logging
import datetime

def login(usr, message):
    LOG_FILENAME = 'log.out'

    timenow = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")

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

