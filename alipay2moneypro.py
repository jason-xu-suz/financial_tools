#!/usr/bin/env python
#  -*- coding: UTF-8 -*-
import logging

from csv_entity.ali_csv import AliCsvRowData
from csv_reader import CsvReader

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

csv_path = 'alipay/test.csv'

# if os.path.isfile(csv_path):
#     with open(csv_path, "r") as csvfile:
#         reader = csv.reader(csvfile)
#         # 这里不需要readlines
#         for line in reader:
#             print line
logger.debug("---")
reader = CsvReader(csv_path)
data_rows = reader.reader_csv()

data_list = []
for row in data_rows:
    if unicode.strip(row[0].decode('utf8')) == u'交易号':
        continue
    else:
        data = AliCsvRowData(row[0],
                             row[1],
                             row[2],
                             row[3],
                             row[4],
                             row[5],
                             row[6],
                             row[7],
                             row[8],
                             row[9],
                             row[10],
                             row[11],
                             row[12],
                             row[13],
                             row[14],
                             row[15]
                             )
        logger.debug(data)
        data_list.append(data)

logger.debug(len(data_list))
