#!/usr/bin/env python

from ..app.connection import Connection, ExchangeTypes
from ..app.broadcaster import Broadcaster

from .arg_parser import first_argument

connection = Connection()
Broadcaster(connection, 'logs', ExchangeTypes.FANOUT).produce(first_argument())
connection.close()
