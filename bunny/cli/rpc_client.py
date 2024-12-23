#!/usr/bin/env python

from ..app.rpc_client import RPCClient
from ..queues.connection import Connection

from .arg_parser import first_argument

connection = Connection()
RPCClient(connection).produce(first_argument())
connection.close()
