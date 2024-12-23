#!/usr/bin/env python

from ..app.router import Router
from ..queues.connection import Connection
from ..queues.types import ExchangeTypes

from .arg_parser import first_argument, second_argument

connection = Connection()
Router(connection, 'routed_logs', ExchangeTypes.DIRECT, first_argument()).produce(second_argument())
connection.close()
