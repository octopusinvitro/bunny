#!/usr/bin/env python

import os
import sys

from ..app.broadcastee import Broadcastee
from ..queues.connection import Connection
from ..queues.types import ExchangeTypes


connection = Connection()

try:
    Broadcastee(connection, 'logs', ExchangeTypes.FANOUT).consume()
except KeyboardInterrupt:
    print('Interrupted')
    try:
        sys.exit(0)
    except SystemExit:
        connection.close()
        os._exit(0)
finally:
    connection.close()
