#!/usr/bin/env python

from ..app.connection import Connection, ExchangeTypes
from ..app.router import Router

from .arg_parser import first_argument, second_argument

connection = Connection()
Router(connection, 'routed_logs', ExchangeTypes.DIRECT, first_argument()).produce(second_argument())
connection.close()
