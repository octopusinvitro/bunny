#!/usr/bin/env python

from ..app.producer import Producer
from ..queues.connection import Connection

from .arg_parser import first_argument

connection = Connection()
Producer(connection).produce(first_argument())
connection.close()
