#!/usr/bin/env python

from ..app.connection import Connection
from ..app.rpc_client import RPCClient

from .arg_parser import first_argument

connection = Connection()
RPCClient(connection).produce(first_argument())
connection.close()
