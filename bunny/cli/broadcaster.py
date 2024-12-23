#!/usr/bin/env python

from ..app.broadcaster import Broadcaster
from ..queues.connection import Connection
from ..queues.types import ExchangeTypes


from .arg_parser import first_argument

connection = Connection()
Broadcaster(connection, 'logs', ExchangeTypes.FANOUT).produce(first_argument())
connection.close()
