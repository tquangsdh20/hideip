class ConnectTimeout(Exception): ...
class ReadTimeout(Exception): ...
class ConnectionError(Exception): ...

__all__ = ['ConnectTimeout', 'ReadTimeout', 'ConnectionError']