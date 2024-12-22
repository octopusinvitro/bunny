#!/usr/bin/env python

import os
import sys

from ..app.connection import Connection, ExchangeTypes
from ..app.routee import Routee

from .arg_parser import all_arguments


connection = Connection()

try:
    Routee(connection, 'filtered_logs', ExchangeTypes.TOPIC, all_arguments()).consume()
except KeyboardInterrupt:
    print('Interrupted')
    try:
        sys.exit(0)
    except SystemExit:
        connection.close()
        os._exit(0)
finally:
    connection.close()
