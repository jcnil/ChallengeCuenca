#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml,os


class Configuration():

    config = yaml.load(open('%s/challenge.conf'% os.path.abspath('.')),Loader=yaml.FullLoader)

    # database postgresql
    DB_HOST = config['postgresql']['host']
    DB_USER = config['postgresql']['user']
    DB_PORT = config['postgresql']['port']
    DB_PASS = config['postgresql']['password']
    DB_NAME = config['postgresql']['name']
