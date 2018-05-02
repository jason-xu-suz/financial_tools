import logging
import os

import csv

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class CsvReader:
    def __init__(self, csv_path):
        self.csv_path = csv_path

    def reader_csv(self):
        if os.path.isfile(self.csv_path):
            logger.debug('Open CSV file:%s' % self.csv_path)
            f = open(self.csv_path, 'rb')
            return csv.reader(f)
        else:
            logger.debug(" %s Is not exists!" % self.csv_path)
