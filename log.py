import logging

LOG_FILENAME = 'log.out'

FORMAT = "%(asctime)-15s %(clientip)s %(user)-8s %(message)s"
logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.DEBUG,
                    format=FORMAT,
                    )

d = {'clientip': '192.168.0.1', 'user': 'nfd5036'}
logging.warning("Attempts: %s", "1", extra=d)

logging.debug('')

f = open(LOG_FILENAME, 'rt')
try:
        body = f.read()
finally:
        f.close()

print 'FILE:'
print body

