#!/usr/bin/env python
# op_cfg.py

import configparser

conf = configparser.ConfigParser()
CONFIGFILE = "cfg/t.cfg"
conf.read(CONFIGFILE, 'UTF-8')


def readCfg():
    sections = conf.sections()
    print(sections)
    print("operation")
    options_sec_a = conf.options('db')
    print(options_sec_a)
    items_sec_a = conf.items('db')
    print(items_sec_a)
    sec_a_key1 = conf.get('db', 'db_host')
    print(sec_a_key1)

if __name__ == '__main__':
    readCfg()
