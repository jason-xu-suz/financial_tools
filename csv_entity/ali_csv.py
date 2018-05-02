#!/usr/bin/python
# -*- coding: UTF-8 -*-


import logging
import os
import time

import csv_entity

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

tim_format = "%Y/%m/%d %H:%M"


class AliCsvRowData:
    tradeNumber = ''

    def __init__(self, trade_number=None, merchant_order_number=None, create_time=None, pay_time=None, last_update_time=None,
                 source=None, trade_type=None, merchant=None, trade_name=None, amount=None, income_or_expenses=None, status=None, service_charge=None,
                 refund=None, remark=None, capital_status=None):
        self.trade_number = trade_number
        self.merchant_order_number = merchant_order_number
        self.create_time = time.mktime(time.strptime(create_time, tim_format)) if str.strip(create_time) != '' else None
        self.pay_time = time.mktime(time.strptime(pay_time, tim_format)) if str.strip(pay_time) != '' else None
        self.last_update_time = time.mktime(time.strptime(last_update_time, tim_format)) if str.strip(last_update_time) != '' else None
        self.source = source
        self.trade_type = trade_type
        self.merchant = merchant
        self.trade_name = trade_name
        self.amount = amount
        self.is_income = (str.strip(income_or_expenses) == '收入')
        self.status = (str.strip(status) == '交易成功')
        self.service_charge = service_charge
        self.refund = refund
        self.remark = remark
        self.capital_status = capital_status

    @staticmethod
    def reader_csv(csv_path):
        if os.path.isfile(csv_path):
            logger.debug('Open CSV file:%s' % csv_path)
            f = open(csv_path, 'rb')
            reader = csv_entity.reader(f)
            data_list = []
            for row in reader:
                if unicode.strip(row[0].decode('utf8')) == u'交易号':
                    continue
                else:
                    # logger.debug(row[0])
                    date = AliCsvRowData(row[0].decode('utf8'),
                                         row[1].decode('utf8'),
                                         row[2],
                                         row[3],
                                         row[4],
                                         row[5].decode('utf8'),
                                         row[6].decode('utf8'),
                                         row[7].decode('utf8'),
                                         row[8].decode('utf8'),
                                         row[9].decode('utf8'),
                                         row[10].decode('utf8'),
                                         row[11].decode('utf8'),
                                         row[12].decode('utf8'),
                                         row[13].decode('utf8'),
                                         row[14].decode('utf8'),
                                         row[15].decode('utf8')
                                         )
                    logger.debug(date)
                    data_list.append(date)
            logger.debug("===")
            return data_list
        else:
            logger.debug(" %s Is not exists!" % csv_path)
