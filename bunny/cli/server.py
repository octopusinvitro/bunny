#!/usr/bin/env python

from ..app.connection import Connection
from ..app.producer import Producer

from .arg_parser import first_argument

connection = Connection()
Producer(connection).produce(first_argument())
connection.close()
