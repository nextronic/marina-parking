import logging
from os.path import dirname

Logger = logging.getLogger('NEXT-DISPLAY')
Logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
fhd = logging.FileHandler(dirname(__file__) + '/../../logs/debug.log')
fhd.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
fhe = logging.FileHandler(dirname(__file__) + '/../../logs/error.log')
fhe.setLevel(logging.ERROR)

# create file handler which logs even debug messages
fhi = logging.FileHandler(dirname(__file__) + '/../../logs/info.log')
fhi.setLevel(logging.INFO)

# create file handler which logs even debug messages
fhw = logging.FileHandler(dirname(__file__) + '/../../logs/warning.log')
fhw.setLevel(logging.WARNING)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fhe.setFormatter(formatter)
ch.setFormatter(formatter)
fhi.setFormatter(formatter)
fhw.setFormatter(formatter)

Logger.addHandler(fhe)
Logger.addHandler(ch)
Logger.addHandler(fhi)
Logger.addHandler(fhw)
