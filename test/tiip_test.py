import json
import unittest

from pytiip.tiip import TIIPMessage
from pytiip import tiip


class TestTIIPMessage(unittest.TestCase):

    def __init__(self, methodName='runTest'):
        unittest.TestCase.__init__(self, methodName)
        self.tiipVersion = tiip.__version__

        # Key examples
        self.timestamp = u'123456789.123'
        self.clientTime = u'987654321.987'
        self.mid = u'testMid'
        self.sid = u'testSid'
        self.type = u'testType'
        self.source = [u'testSource1', u'testSource2']
        self.pid = u'testPid'
        self.target = u'testTarget'
        self.subTarget = u'testSubTarget'
        self.signal = u'testSignal'
        self.arguments = {u'testArgument1': u'testArgumentValue1', u'testArgument2': u'testArgumentValue2'}
        self.payload = [u'testPayloadValue1', u'testPayloadValue2']
        self.ok = True
        self.tenant = u'testTenant'

        # Dictionary representation example
        self.tiipDict = {
            'timestamp': self.timestamp,
            'clientTime': self.clientTime,
            'mid': self.mid,
            'sid': self.sid,
            'type': self.type,
            'source': self.source,
            'pid': self.pid,
            'target': self.target,
            'subTarget': self.subTarget,
            'signal': self.signal,
            'arguments': self.arguments,
            'payload': self.payload,
            'ok': self.ok,
            'tenant': self.tenant
        }

        # String representation example
        self.tiipStr = json.dumps(self.tiipDict)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def generateExampleTIIPMessage(self):
        return TIIPMessage(timestamp=self.timestamp, clientTime=self.clientTime, mid=self.mid, sid=self.sid,
                           type=self.type, source=self.source, pid=self.pid, target=self.target, subTarget=self.subTarget,
                           signal=self.signal, arguments=self.arguments, payload=self.payload, ok=self.ok, tenant=self.tenant)

    def verifyKeys(self, tiipMsg):
        self.assertEquals(tiipMsg.timestamp, self.timestamp)
        self.assertEquals(tiipMsg.clientTime, self.clientTime)
        self.assertEquals(tiipMsg.mid, self.mid)
        self.assertEquals(tiipMsg.sid, self.sid)
        self.assertEquals(tiipMsg.type, self.type)
        self.assertEquals(tiipMsg.source, self.source)
        self.assertEquals(tiipMsg.pid, self.pid)
        self.assertEquals(tiipMsg.target, self.target)
        self.assertEquals(tiipMsg.subTarget, self.subTarget)
        self.assertEquals(tiipMsg.signal, self.signal)
        self.assertEquals(tiipMsg.arguments, self.arguments)
        self.assertEquals(tiipMsg.payload, self.payload)
        self.assertEquals(tiipMsg.ok, self.ok)
        self.assertEquals(tiipMsg.tenant, self.tenant)

    def test000_initFromKeys(self):
        tiipMsg = self.generateExampleTIIPMessage()
        self.verifyKeys(tiipMsg)

    def test001_initFromDict(self):
        tiipMsg = TIIPMessage(tiipDict=self.tiipDict)
        self.verifyKeys(tiipMsg)

    def test002_initFromStr(self):
        tiipMsg = TIIPMessage(tiipStr=self.tiipStr)
        self.verifyKeys(tiipMsg)

    def test003_verifyProtocol(self):
        """
        Test that protocol key is automatically generated to be the version of the protocol
        """
        tiipMsgEmpty = TIIPMessage()
        self.assertEquals(tiipMsgEmpty.protocol, self.tiipVersion)
        tiipMsgFromKeys = self.generateExampleTIIPMessage()
        self.assertEquals(tiipMsgFromKeys.protocol, self.tiipVersion)
        tiipMsgFromDict = TIIPMessage(tiipDict=self.tiipDict)
        self.assertEquals(tiipMsgFromDict.protocol, self.tiipVersion)
        tiipMsgFromStr = TIIPMessage(tiipStr=self.tiipStr)
        self.assertEquals(tiipMsgFromStr.protocol, self.tiipVersion)

    def test004_verifyTimestamp(self):
        """
        Test that a timestamp is automatically generated if not specified.
        """
        tiipMsg = TIIPMessage()
        self.assertIsInstance(tiipMsg.timestamp, basestring)
        float(tiipMsg.timestamp)  # Make sure the timestamp is a str representation of a float

    def test005_setProtocol(self):
        tiipMessage = TIIPMessage()
        # Make sure that attempts to set protocol key raises exception
        with self.assertRaises(AttributeError):
            # noinspection PyPropertyAccess
            tiipMessage.protocol = 'myProtocol'

    def test006_setTimestamp(self):
        tiipMessage = TIIPMessage()

        # Correct (str, unicode, float, int, long)
        tiipMessage.timestamp = str(self.timestamp)
        self.assertEquals(tiipMessage.timestamp, self.timestamp)
        tiipMessage.timestamp = self.timestamp
        self.assertEquals(tiipMessage.timestamp, self.timestamp)
        tiipMessage.timestamp = float(self.timestamp)
        self.assertEquals(tiipMessage.timestamp, self.timestamp)
        tiipMessage.timestamp = int(float(self.timestamp))
        self.assertEquals(tiipMessage.timestamp, repr(round(int(float(self.timestamp)), 3)))
        tiipMessage.timestamp = long(float(self.timestamp))
        self.assertEquals(tiipMessage.timestamp, repr(round(long(float(self.timestamp)), 3)))

        # Incorrect
        tiipMessage = TIIPMessage()
        with self.assertRaises(ValueError):
            tiipMessage.timestamp = None
        with self.assertRaises(ValueError):
            tiipMessage.timestamp = 'incorrectTimestampString'

    def test007_setClientTime(self):
        # Correct (str, unicode, float, int, long, None)
        tiipMessage = TIIPMessage()
        tiipMessage.clientTime = str(self.clientTime)
        self.assertEquals(tiipMessage.clientTime, self.clientTime)
        tiipMessage.clientTime = self.clientTime
        self.assertEquals(tiipMessage.clientTime, self.clientTime)
        tiipMessage.clientTime = float(self.clientTime)
        self.assertEquals(tiipMessage.clientTime, self.clientTime)
        tiipMessage.clientTime = int(float(self.clientTime))
        self.assertEquals(tiipMessage.clientTime, repr(round(int(float(self.clientTime)), 3)))
        tiipMessage.clientTime = long(float(self.clientTime))
        self.assertEquals(tiipMessage.clientTime, repr(round(long(float(self.clientTime)), 3)))
        tiipMessage.clientTime = None
        self.assertEquals(tiipMessage.clientTime, None)

        # Incorrect
        tiipMessage = TIIPMessage()
        with self.assertRaises(ValueError):
            tiipMessage.clientTime = 'incorrectClientTimeStampString'

    def test008_setMid(self):
        # Correct (str, unicode, None)
        tiipMessage = TIIPMessage()
        tiipMessage.mid = str(self.mid)
        self.assertEquals(tiipMessage.mid, self.mid)
        tiipMessage.mid = self.mid
        self.assertEquals(tiipMessage.mid, self.mid)
        tiipMessage.mid = None
        self.assertEquals(tiipMessage.mid, None)

    def test009_setSid(self):
        # Correct (str, unicode, None)
        tiipMessage = TIIPMessage()
        tiipMessage.sid = str(self.sid)
        self.assertEquals(tiipMessage.sid, self.sid)
        tiipMessage.sid = self.sid
        self.assertEquals(tiipMessage.sid, self.sid)
        tiipMessage.sid = None
        self.assertEquals(tiipMessage.sid, None)

        # Incorrect
        with self.assertRaises(ValueError):
            tiipMessage.sid = 1

    def test010_setType(self):
        # Correct (str, unicode, None)
        tiipMessage = TIIPMessage()
        tiipMessage.type = str(self.type)
        self.assertEquals(tiipMessage.type, self.type)
        tiipMessage.type = self.type
        self.assertEquals(tiipMessage.type, self.type)
        tiipMessage.type = None
        self.assertEquals(tiipMessage.type, None)

        # Incorrect
        with self.assertRaises(ValueError):
            tiipMessage.type = 1

    def test011_setSource(self):
        # Correct (list, None)
        tiipMessage = TIIPMessage()
        tiipMessage.source = self.source
        self.assertEquals(tiipMessage.source, self.source)
        tiipMessage.source = None
        self.assertEquals(tiipMessage.source, None)

        # Incorrect
        with self.assertRaises(ValueError):
            tiipMessage.source = 1

    def test012_setPid(self):
        # Correct (str, unicode, None)
        tiipMessage = TIIPMessage()
        tiipMessage.pid = str(self.pid)
        self.assertEquals(tiipMessage.pid, self.pid)
        tiipMessage.pid = self.pid
        self.assertEquals(tiipMessage.pid, self.pid)
        tiipMessage.pid = None
        self.assertEquals(tiipMessage.pid, None)

        # Incorrect
        with self.assertRaises(ValueError):
            tiipMessage.pid = 1

    def test013_setTarget(self):
        # Correct (str, unicode, None)
        tiipMessage = TIIPMessage()
        tiipMessage.target = str(self.target)
        self.assertEquals(tiipMessage.target, self.target)
        tiipMessage.target = self.target
        self.assertEquals(tiipMessage.target, self.target)
        tiipMessage.target = None
        self.assertEquals(tiipMessage.target, None)

        # Incorrect
        with self.assertRaises(ValueError):
            tiipMessage.target = 1

    def test014_setSubTarget(self):
        # Correct (str, unicode, None)
        tiipMessage = TIIPMessage()
        tiipMessage.subTarget = str(self.subTarget)
        self.assertEquals(tiipMessage.subTarget, self.subTarget)
        tiipMessage.subTarget = self.subTarget
        self.assertEquals(tiipMessage.subTarget, self.subTarget)
        tiipMessage.subTarget = None
        self.assertEquals(tiipMessage.subTarget, None)

        # Incorrect
        with self.assertRaises(ValueError):
            tiipMessage.subTarget = 1

    def test015_setSignal(self):
        # Correct (str, unicode, None)
        tiipMessage = TIIPMessage()
        tiipMessage.signal = str(self.signal)
        self.assertEquals(tiipMessage.signal, self.signal)
        tiipMessage.signal = self.signal
        self.assertEquals(tiipMessage.signal, self.signal)
        tiipMessage.signal = None
        self.assertEquals(tiipMessage.signal, None)

        # Incorrect
        with self.assertRaises(ValueError):
            tiipMessage.signal = 1

    def test016_setArguments(self):
        # Correct (dict, None)
        tiipMessage = TIIPMessage()
        tiipMessage.arguments = self.arguments
        self.assertEquals(tiipMessage.arguments, self.arguments)
        tiipMessage.arguments = None
        self.assertEquals(tiipMessage.arguments, None)

        # Incorrect
        with self.assertRaises(ValueError):
            tiipMessage.arguments = 1

    def test017_setPayload(self):
        # Correct (list, None)
        tiipMessage = TIIPMessage()
        tiipMessage.payload = self.payload
        self.assertEquals(tiipMessage.payload, self.payload)
        tiipMessage.payload = None
        self.assertEquals(tiipMessage.payload, None)

        # Incorrect
        with self.assertRaises(ValueError):
            tiipMessage.payload = 1

    def test018_setOk(self):
        # Correct (bool, None)
        tiipMessage = TIIPMessage()
        tiipMessage.ok = self.ok
        self.assertEquals(tiipMessage.ok, self.ok)
        tiipMessage.ok = None
        self.assertEquals(tiipMessage.ok, None)

        # Incorrect
        with self.assertRaises(ValueError):
            tiipMessage.ok = 1

    def test019_setTenant(self):
        # Correct (str, unicode, None)
        tiipMessage = TIIPMessage()
        tiipMessage.tenant = str(self.tenant)
        self.assertEquals(tiipMessage.tenant, self.tenant)
        tiipMessage.tenant = self.tenant
        self.assertEquals(tiipMessage.tenant, self.tenant)
        tiipMessage.tenant = None
        self.assertEquals(tiipMessage.tenant, None)

        # Incorrect
        with self.assertRaises(ValueError):
            tiipMessage.tenant = 1

    def test020_strCast(self):
        tiipMessage = self.generateExampleTIIPMessage()
        self.assertEquals(json.loads(str(tiipMessage)), dict(self.tiipDict, protocol=self.tiipVersion))

    def test021_dictCast(self):
        tiipMessage = self.generateExampleTIIPMessage()
        self.assertEquals(dict(tiipMessage), dict(self.tiipDict, protocol=self.tiipVersion))

if __name__ == "__main__":
    unittest.main()
