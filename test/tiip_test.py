import json
import unittest

from pytiip.tiip import TIIPMessage
from pytiip import tiip
import sys
PY3 = sys.version_info > (3,)
if PY3:
    long = int
    unicode = str
    basestring = str
else:
    # noinspection PyShadowingBuiltins
    bytes = str


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
        self.target = [u'testTarget1', u'testTarget2']
        self.signal = u'testSignal'
        self.channel = u'testChannel'
        self.arguments = {u'testArgument1': u'testArgumentValue1', u'testArgument2': u'testArgumentValue2'}
        self.payload = [u'testPayloadValue1', u'testPayloadValue2']
        self.ok = True
        self.tenant = u'testTenant'

        # Dictionary representation example
        self.tiipDict = {
            'pv': self.tiipVersion,
            'ts': self.timestamp,
            'ct': self.clientTime,
            'mid': self.mid,
            'sid': self.sid,
            'type': self.type,
            'src': self.source,
            'targ': self.target,
            'sig': self.signal,
            'ch': self.channel,
            'arg': self.arguments,
            'pl': self.payload,
            'ok': self.ok,
            'ten': self.tenant
        }

        # String representation example
        self.tiipStr = json.dumps(self.tiipDict)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def generateExampleTIIPMessage(self):
        return TIIPMessage(
            ts=self.timestamp, ct=self.clientTime, mid=self.mid, sid=self.sid, type=self.type,
            src=self.source, targ=self.target, sig=self.signal, ch=self.channel,
            arg=self.arguments, pl=self.payload, ok=self.ok, ten=self.tenant)

    def verifyKeys(self, tiipMsg):
        self.assertEquals(tiipMsg.ts, self.timestamp)
        self.assertEquals(tiipMsg.ct, self.clientTime)
        self.assertEquals(tiipMsg.mid, self.mid)
        self.assertEquals(tiipMsg.sid, self.sid)
        self.assertEquals(tiipMsg.type, self.type)
        self.assertEquals(tiipMsg.src, self.source)
        self.assertEquals(tiipMsg.targ, self.target)
        self.assertEquals(tiipMsg.sig, self.signal)
        self.assertEquals(tiipMsg.ch, self.channel)
        self.assertEquals(tiipMsg.arg, self.arguments)
        self.assertEquals(tiipMsg.pl, self.payload)
        self.assertEquals(tiipMsg.ok, self.ok)
        self.assertEquals(tiipMsg.ten, self.tenant)

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
        self.assertEquals(tiipMsgEmpty.pv, self.tiipVersion)
        tiipMsgFromKeys = self.generateExampleTIIPMessage()
        self.assertEquals(tiipMsgFromKeys.pv, self.tiipVersion)
        tiipMsgFromDict = TIIPMessage(tiipDict=self.tiipDict)
        self.assertEquals(tiipMsgFromDict.pv, self.tiipVersion)
        tiipMsgFromStr = TIIPMessage(tiipStr=self.tiipStr)
        self.assertEquals(tiipMsgFromStr.pv, self.tiipVersion)

    def test004_verifyTimestamp(self):
        """
        Test that a timestamp is automatically generated if not specified.
        """
        tiipMsg = TIIPMessage()
        self.assertIsInstance(tiipMsg.ts, basestring)
        float(tiipMsg.ts)  # Make sure the timestamp is a str representation of a float

    def test005_setProtocol(self):
        tiipMessage = TIIPMessage()
        # Make sure that attempts to set protocol key raises exception
        with self.assertRaises(AttributeError):
            # noinspection PyPropertyAccess
            tiipMessage.protocol = 'myProtocol'

    def test006_setTimestamp(self):
        tiipMessage = TIIPMessage()

        # Correct (str, unicode, float, int, long)
        tiipMessage.ts = str(self.timestamp)
        self.assertEquals(tiipMessage.ts, self.timestamp)
        tiipMessage.ts = self.timestamp
        self.assertEquals(tiipMessage.ts, self.timestamp)
        tiipMessage.ts = float(self.timestamp)
        self.assertEquals(tiipMessage.ts, self.timestamp)
        tiipMessage.ts = int(float(self.timestamp))
        self.assertEquals(tiipMessage.ts, repr(round(int(float(self.timestamp)), 3)))
        tiipMessage.ts = long(float(self.timestamp))
        self.assertEquals(tiipMessage.ts, repr(round(long(float(self.timestamp)), 3)))

        # Incorrect
        tiipMessage = TIIPMessage()
        with self.assertRaises(TypeError):
            tiipMessage.ts = None
        with self.assertRaises(ValueError):
            tiipMessage.ts = 'incorrectTimestampString'

    def test007_setClientTime(self):
        # Correct (str, unicode, float, int, long, None)
        tiipMessage = TIIPMessage()
        tiipMessage.ct = str(self.clientTime)
        self.assertEquals(tiipMessage.ct, self.clientTime)
        tiipMessage.ct = self.clientTime
        self.assertEquals(tiipMessage.ct, self.clientTime)
        tiipMessage.ct = float(self.clientTime)
        self.assertEquals(tiipMessage.ct, self.clientTime)
        tiipMessage.ct = int(float(self.clientTime))
        self.assertEquals(tiipMessage.ct, repr(round(int(float(self.clientTime)), 3)))
        tiipMessage.ct = long(float(self.clientTime))
        self.assertEquals(tiipMessage.ct, repr(round(long(float(self.clientTime)), 3)))
        tiipMessage.ct = None
        self.assertEquals(tiipMessage.ct, None)

        # Incorrect
        tiipMessage = TIIPMessage()
        with self.assertRaises(ValueError):
            tiipMessage.ct = 'incorrectClientTimeStampString'
        with self.assertRaises(TypeError):
            tiipMessage.ts = dict()

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
        with self.assertRaises(TypeError):
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
        with self.assertRaises(TypeError):
            tiipMessage.type = 1

    def test011_setSource(self):
        # Correct (list, None)
        tiipMessage = TIIPMessage()
        tiipMessage.src = self.source
        self.assertEquals(tiipMessage.src, self.source)
        tiipMessage.src = None
        self.assertEquals(tiipMessage.src, None)

        # Incorrect
        with self.assertRaises(TypeError):
            tiipMessage.src = 1

    def test012_setTarget(self):
        # Correct (str, unicode, None)
        tiipMessage = TIIPMessage()
        tiipMessage.targ = self.target
        self.assertEquals(tiipMessage.targ, self.target)
        tiipMessage.targ = None
        self.assertEquals(tiipMessage.targ, None)

        # Incorrect
        with self.assertRaises(TypeError):
            tiipMessage.targ = 1

    def test014_setSignal(self):
        # Correct (str, unicode, None)
        tiipMessage = TIIPMessage()
        tiipMessage.sig = str(self.signal)
        self.assertEquals(tiipMessage.sig, self.signal)
        tiipMessage.sig = self.signal
        self.assertEquals(tiipMessage.sig, self.signal)
        tiipMessage.sig = None
        self.assertEquals(tiipMessage.sig, None)

        # Incorrect
        with self.assertRaises(TypeError):
            tiipMessage.sig = 1

    def test015_setArguments(self):
        # Correct (dict, None)
        tiipMessage = TIIPMessage()
        tiipMessage.arg = self.arguments
        self.assertEquals(tiipMessage.arg, self.arguments)
        tiipMessage.arg = None
        self.assertEquals(tiipMessage.arg, None)

        # Incorrect
        with self.assertRaises(TypeError):
            tiipMessage.arg = 1

    def test016_setPayload(self):
        # Correct (list, None)
        tiipMessage = TIIPMessage()
        tiipMessage.pl = self.payload
        self.assertEquals(tiipMessage.pl, self.payload)
        tiipMessage.pl = None
        self.assertEquals(tiipMessage.pl, None)

        # Incorrect
        with self.assertRaises(TypeError):
            tiipMessage.pl = 1

    def test017_setOk(self):
        # Correct (bool, None)
        tiipMessage = TIIPMessage()
        tiipMessage.ok = self.ok
        self.assertEquals(tiipMessage.ok, self.ok)
        tiipMessage.ok = None
        self.assertEquals(tiipMessage.ok, None)

        # Incorrect
        with self.assertRaises(TypeError):
            tiipMessage.ok = 1

    def test018_setTenant(self):
        # Correct (str, unicode, None)
        tiipMessage = TIIPMessage()
        tiipMessage.ten = str(self.tenant)
        self.assertEquals(tiipMessage.ten, self.tenant)
        tiipMessage.ten = self.tenant
        self.assertEquals(tiipMessage.ten, self.tenant)
        tiipMessage.ten = None
        self.assertEquals(tiipMessage.ten, None)

        # Incorrect
        with self.assertRaises(TypeError):
            tiipMessage.ten = 1

    def test019_strCast(self):
        tiipMessage = self.generateExampleTIIPMessage()
        self.assertEquals(json.loads(str(tiipMessage)), dict(self.tiipDict, protocol=self.tiipVersion))

    def test020_dictCast(self):
        tiipMessage = self.generateExampleTIIPMessage()
        self.assertEquals(dict(tiipMessage), dict(self.tiipDict, protocol=self.tiipVersion))

    def test021_setChannel(self):
        # Correct (str, unicode, None)
        tiipMessage = TIIPMessage()
        tiipMessage.ch = str(self.channel)
        self.assertEquals(tiipMessage.ch, self.channel)
        tiipMessage.ch = self.channel
        self.assertEquals(tiipMessage.ch, self.channel)
        tiipMessage.ch = None
        self.assertEquals(tiipMessage.ch, None)

        # Incorrect
        with self.assertRaises(TypeError):
            tiipMessage.sig = 1

if __name__ == "__main__":
    unittest.main()
