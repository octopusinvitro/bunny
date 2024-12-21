#!/usr/bin/env python

import os
import sys

from ..app.connection import Connection
from ..app.consumer import Consumer


connection = Connection()

try:
    Consumer(connection).consume()
except KeyboardInterrupt:
    print('Interrupted')
    try:
        sys.exit(0)
    except SystemExit:
        connection.close()
        os._exit(0)
finally:
    connection.close()
