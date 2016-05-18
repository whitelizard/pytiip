"""
Python implementation of the TIIP (Thin Industrial Internet Protocol) protocol.
"""

import json
import time


__version__ = 'tiip0.9'


class TIIPMessage(object):
    # noinspection PyShadowingBuiltins
    def __init__(self, tiipStr=None, tiipDict=None, timestamp=None, clientTime=None, mid=None, sid=None, type=None, source=None,
                 pid=None, target=None, subTarget=None, signal=None, arguments=None, payload=None, ok=None, tenant=None):
        """
        @param tiipStr: A string representation of a TIIPMessage to load on init
        @param tiipDict: A dictionary representation of a TIIPMessage to load on init
        @raise: TypeError, ValueError
        All other arguments are keys to set in the TIIPMessage, see TIIP specification for more details:
            https://github.com/whitelizard/tiip
        """
        # Protocol keys
        self.__protocol = __version__
        self.__timestamp = self.__getTimeStamp()
        self.__clientTime = None
        self.__mid = None
        self.__sid = None
        self.__type = None
        self.__source = None
        self.__pid = None  # DEPRECATED!
        self.__target = None
        self.__subTarget = None
        self.__signal = None
        self.__arguments = None
        self.__payload = None
        self.__ok = None
        self.__tenant = None

        # Parse constructor arguments
        if tiipStr is not None:
            self.loadFromStr(tiipStr)
        if tiipDict is not None:
            self.loadFromDict(tiipDict)
        if timestamp is not None:
            self.timestamp = timestamp
        if clientTime is not None:
            self.clientTime = clientTime
        if mid is not None:
            self.mid = mid
        if sid is not None:
            self.sid = sid
        if type is not None:
            self.type = type
        if source is not None:
            self.source = source
        if pid is not None:
            self.pid = pid  # DEPRECATED!
        if target is not None:
            self.target = target
        if subTarget is not None:
            self.subTarget = subTarget
        if signal is not None:
            self.signal = signal
        if arguments is not None:
            self.arguments = arguments
        if payload is not None:
            self.payload = payload
        if ok is not None:
            self.ok = ok
        if tenant is not None:
            self.tenant = tenant

    def __str__(self):
        return json.dumps(dict(self))

    def __iter__(self):
        yield 'protocol', self.__protocol
        yield 'timestamp', self.__timestamp
        if self.__clientTime is not None:
            yield 'clientTime', self.__clientTime
        if self.__mid is not None:
            yield 'mid', self.__mid
        if self.__sid is not None:
            yield 'sid', self.__sid
        if self.__type is not None:
            yield 'type', self.__type
        if self.__source is not None:
            yield 'source', self.__source
        if self.__pid is not None:  # DEPRECATED!
            yield 'pid', self.__pid
        if self.__target is not None:
            yield 'target', self.__target
        if self.__subTarget is not None:
            yield 'subTarget', self.__subTarget
        if self.__signal is not None:
            yield 'signal', self.__signal
        if self.__arguments is not None:
            yield 'arguments', self.__arguments
        if self.__payload is not None:
            yield 'payload', self.__payload
        if self.__ok is not None:
            yield 'ok', self.__ok
        if self.__tenant is not None:
            yield 'tenant', self.__tenant

    @staticmethod
    def __getTimeStamp():
        """
        Creates a timestamp string representation according to the TIIP-specification for timestamps.
        @return:
        """
        return repr(round(time.time(), 3))

    @property
    def protocol(self):
        return self.__protocol

    @property
    def timestamp(self):
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, value):
        if isinstance(value, basestring):
            try:
                float(value)  # Check if string is float representation
            except ValueError:
                raise ValueError('timestamp string must be parseable to float')
            else:
                self.__timestamp = value
        elif isinstance(value, (int, float, long)):
            self.__timestamp = repr(round(value, 3))
        else:
            raise TypeError('timestamp can only be of types float, int, long or a valid unicode or string representation of a float')

    @property
    def clientTime(self):
        return self.__clientTime

    @clientTime.setter
    def clientTime(self, value):
        if value is None:
            self.__clientTime = None
        elif isinstance(value, basestring):
            try:
                float(value)  # Check if string is float representation
            except ValueError:
                raise ValueError('clientTime string must be parseable to float')
            else:
                self.__clientTime = value
        elif isinstance(value, (int, float, long)):
            self.__clientTime = repr(round(value, 3))
        else:
            raise TypeError('clientTime can only be of types None, float, int, long or a valid unicode or string representation of a float')

    @property
    def mid(self):
        return self.__mid

    @mid.setter
    def mid(self, value):
        if value is None:
            self.__mid = None
        elif isinstance(value, basestring):
            self.__mid = value
        else:
            raise TypeError('mid can only be of types unicode, str or None')

    @property
    def sid(self):
        return self.__sid

    @sid.setter
    def sid(self, value):
        if value is None:
            self.__sid = None
        elif isinstance(value, basestring):
            self.__sid = value
        else:
            raise TypeError('sid can only be of types unicode, str or None')

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        if value is None:
            self.__type = None
        elif isinstance(value, basestring):
            self.__type = value
        else:
            raise TypeError('type can only be of types unicode, str or None')

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        if value is None:
            self.__source = None
        elif isinstance(value, list):
            self.__source = value
        else:
            raise TypeError('source can only be of types list or None')

    # DEPRECATED!
    @property
    def pid(self):
        return self.__pid

    # DEPRECATED!
    @pid.setter
    def pid(self, value):
        if value is None:
            self.__pid = None
        elif isinstance(value, basestring):
            self.__pid = value
        else:
            raise TypeError('pid can only be of types unicode, str or None')

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        if value is None:
            self.__target = None
        elif isinstance(value, basestring):
            self.__target = value
        else:
            raise TypeError('target can only be of types unicode, str or None')

    @property
    def subTarget(self):
        return self.__subTarget

    @subTarget.setter
    def subTarget(self, value):
        if value is None:
            self.__subTarget = None
        elif isinstance(value, basestring):
            self.__subTarget = value
        else:
            raise TypeError('subTarget can only be of types unicode, str or None')

    @property
    def signal(self):
        return self.__signal

    @signal.setter
    def signal(self, value):
        if value is None:
            self.__signal = None
        elif isinstance(value, basestring):
            self.__signal = value
        else:
            raise TypeError('signal can only be of types unicode, str or None')

    @property
    def arguments(self):
        return self.__arguments

    @arguments.setter
    def arguments(self, value):
        if value is None:
            self.__arguments = None
        elif isinstance(value, dict):
            self.__arguments = value
        else:
            raise TypeError('arguments can only be of types dict or None')

    @property
    def payload(self):
        return self.__payload

    @payload.setter
    def payload(self, value):
        if value is None:
            self.__payload = None
        elif isinstance(value, list):
            self.__payload = value
        else:
            raise TypeError('payload can only be of types dict or None')

    @property
    def ok(self):
        return self.__ok

    @ok.setter
    def ok(self, value):
        if value is None:
            self.__ok = None
        elif isinstance(value, bool):
            self.__ok = value
        else:
            raise TypeError('ok can only be of types bool or None')

    @property
    def tenant(self):
        return self.__tenant

    @tenant.setter
    def tenant(self, value):
        if value is None:
            self.__tenant = None
        elif isinstance(value, basestring):
            self.__tenant = value
        else:
            raise TypeError('tenant can only be of types unicode, str or None')

    def loadFromStr(self, tiipStr):
        """
        Loads this object with values from a string or unicode representation of a TIIPMessage.
        @param tiipStr: The string to load properties from.
        @raise: TypeError, ValueError
        @return: None
        """
        tiipDict = json.loads(tiipStr)
        self.loadFromDict(tiipDict)

    def loadFromDict(self, tiipDict):
        """
        Loads this object with values from a dictionary representation of a TIIPMessage.
        @param tiipDict: The dictionary to load properties from.
        @raise: TypeError, ValueError
        @return: None
        """
        if 'timestamp' in tiipDict:
            self.timestamp = tiipDict['timestamp']
        if 'clientTime' in tiipDict:
            self.clientTime = tiipDict['clientTime']
        if 'mid' in tiipDict:
            self.mid = tiipDict['mid']
        if 'sid' in tiipDict:
            self.sid = tiipDict['sid']
        if 'type' in tiipDict:
            self.type = tiipDict['type']
        if 'source' in tiipDict:
            self.source = tiipDict['source']
        if 'pid' in tiipDict:
            self.pid = tiipDict['pid']
        if 'target' in tiipDict:
            self.target = tiipDict['target']
        if 'subTarget' in tiipDict:
            self.subTarget = tiipDict['subTarget']
        if 'signal' in tiipDict:
            self.signal = tiipDict['signal']
        if 'arguments' in tiipDict:
            self.arguments = tiipDict['arguments']
        if 'payload' in tiipDict:
            self.payload = tiipDict['payload']
        if 'ok' in tiipDict:
            self.ok = tiipDict['ok']
        if 'tenant' in tiipDict:
            self.tenant = tiipDict['tenant']
