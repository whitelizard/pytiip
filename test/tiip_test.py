import json
import unittest
import dateutil.parser as parser

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
        self.timestamp = u'2000-01-01T01:23:45.678901Z'
        self.latency = u'987654321.987'
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
            'lat': self.latency,
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
            ts=self.timestamp, lat=self.latency, mid=self.mid, sid=self.sid, type=self.type,
            src=self.source, targ=self.target, sig=self.signal, ch=self.channel,
            arg=self.arguments, pl=self.payload, ok=self.ok, ten=self.tenant)

    def verifyKeys(self, tiipMsg):
        self.assertEqual(tiipMsg.ts, self.timestamp)
        self.assertEqual(tiipMsg.lat, self.latency)
        self.assertEqual(tiipMsg.mid, self.mid)
        self.assertEqual(tiipMsg.sid, self.sid)
        self.assertEqual(tiipMsg.type, self.type)
        self.assertEqual(tiipMsg.src, self.source)
        self.assertEqual(tiipMsg.targ, self.target)
        self.assertEqual(tiipMsg.sig, self.signal)
        self.assertEqual(tiipMsg.ch, self.channel)
        self.assertEqual(tiipMsg.arg, self.arguments)
        self.assertEqual(tiipMsg.pl, self.payload)
        self.assertEqual(tiipMsg.ok, self.ok)
        self.assertEqual(tiipMsg.ten, self.tenant)

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
        self.assertEqual(tiipMsgEmpty.pv, self.tiipVersion)
        tiipMsgFromKeys = self.generateExampleTIIPMessage()
        self.assertEqual(tiipMsgFromKeys.pv, self.tiipVersion)
        tiipMsgFromDict = TIIPMessage(tiipDict=self.tiipDict)
        self.assertEqual(tiipMsgFromDict.pv, self.tiipVersion)
        tiipMsgFromStr = TIIPMessage(tiipStr=self.tiipStr)
        self.assertEqual(tiipMsgFromStr.pv, self.tiipVersion)

    def test004_verifyTimestamp(self):
        """
        Test that a timestamp is automatically generated if not specified.
        """
        tiipMsg = TIIPMessage()
        self.assertIsInstance(tiipMsg.ts, basestring)
        parser.parse(tiipMsg.ts)  # Make sure the timestamp is a str representation of a float

    def test005_setProtocol(self):
        tiipMessage = TIIPMessage()
        # Make sure that attempts to set protocol key raises exception
        with self.assertRaises(AttributeError):
            # noinspection PyPropertyAccess
            tiipMessage.pv = 'myProtocol'

    def test006_setTimestamp(self):
        tiipMessage = TIIPMessage()

        # Correct (str, unicode, float, int, long)
        tiipMessage.ts = str(self.timestamp)
        self.assertEqual(tiipMessage.ts, self.timestamp)
        tiipMessage.ts = self.timestamp
        self.assertEqual(tiipMessage.ts, self.timestamp)
        tiipMessage.ts = parser.parse(self.timestamp)
        print(tiipMessage.ts)
        self.assertEqual(tiipMessage.ts, self.timestamp)

        # Incorrect
        tiipMessage = TIIPMessage()
        with self.assertRaises(TypeError):
            tiipMessage.ts = None
        with self.assertRaises(ValueError):
            tiipMessage.ts = 'incorrectTimestampString'

    def test007_setLatency(self):
        # Correct (str, unicode, float, int, long, None)
        tiipMessage = TIIPMessage()
        tiipMessage.lat = str(self.latency)
        self.assertEqual(tiipMessage.lat, self.latency)
        tiipMessage.lat = self.latency
        self.assertEqual(tiipMessage.lat, self.latency)
        tiipMessage.lat = float(self.latency)
        self.assertEqual(tiipMessage.lat, self.latency)
        tiipMessage.lat = int(float(self.latency))
        self.assertEqual(tiipMessage.lat, repr(round(int(float(self.latency)), 3)))
        tiipMessage.lat = long(float(self.latency))
        self.assertEqual(tiipMessage.lat, repr(round(long(float(self.latency)), 3)))
        tiipMessage.lat = None
        self.assertEqual(tiipMessage.lat, None)

        # Incorrect
        tiipMessage = TIIPMessage()
        with self.assertRaises(ValueError):
            tiipMessage.lat = 'incorrectClientTimeStampString'
        with self.assertRaises(TypeError):
            tiipMessage.ts = dict()

    def test008_setMid(self):
        # Correct (str, unicode, None)
        tiipMessage = TIIPMessage()
        tiipMessage.mid = str(self.mid)
        self.assertEqual(tiipMessage.mid, self.mid)
        tiipMessage.mid = self.mid
        self.assertEqual(tiipMessage.mid, self.mid)
        tiipMessage.mid = None
        self.assertEqual(tiipMessage.mid, None)

    def test009_setSid(self):
        # Correct (str, unicode, None)
        tiipMessage = TIIPMessage()
        tiipMessage.sid = str(self.sid)
        self.assertEqual(tiipMessage.sid, self.sid)
        tiipMessage.sid = self.sid
        self.assertEqual(tiipMessage.sid, self.sid)
        tiipMessage.sid = None
        self.assertEqual(tiipMessage.sid, None)

        # Incorrect
        with self.assertRaises(TypeError):
            tiipMessage.sid = 1

    def test010_setType(self):
        # Correct (str, unicode, None)
        tiipMessage = TIIPMessage()
        tiipMessage.type = str(self.type)
        self.assertEqual(tiipMessage.type, self.type)
        tiipMessage.type = self.type
        self.assertEqual(tiipMessage.type, self.type)
        tiipMessage.type = None
        self.assertEqual(tiipMessage.type, None)

        # Incorrect
        with self.assertRaises(TypeError):
            tiipMessage.type = 1

    def test011_setSource(self):
        # Correct (list, None)
        tiipMessage = TIIPMessage()
        tiipMessage.src = self.source
        self.assertEqual(tiipMessage.src, self.source)
        tiipMessage.src = None
        self.assertEqual(tiipMessage.src, None)

        # Incorrect
        with self.assertRaises(TypeError):
            tiipMessage.src = 1

    def test012_setTarget(self):
        # Correct (str, unicode, None)
        tiipMessage = TIIPMessage()
        tiipMessage.targ = self.target
        self.assertEqual(tiipMessage.targ, self.target)
        tiipMessage.targ = None
        self.assertEqual(tiipMessage.targ, None)

        # Incorrect
        with self.assertRaises(TypeError):
            tiipMessage.targ = 1

    def test014_setSignal(self):
        # Correct (str, unicode, None)
        tiipMessage = TIIPMessage()
        tiipMessage.sig = str(self.signal)
        self.assertEqual(tiipMessage.sig, self.signal)
        tiipMessage.sig = self.signal
        self.assertEqual(tiipMessage.sig, self.signal)
        tiipMessage.sig = None
        self.assertEqual(tiipMessage.sig, None)

        # Incorrect
        with self.assertRaises(TypeError):
            tiipMessage.sig = 1

    def test015_setArguments(self):
        # Correct (dict, None)
        tiipMessage = TIIPMessage()
        tiipMessage.arg = self.arguments
        self.assertEqual(tiipMessage.arg, self.arguments)
        tiipMessage.arg = None
        self.assertEqual(tiipMessage.arg, None)

        # Incorrect
        with self.assertRaises(TypeError):
            tiipMessage.arg = 1

    def test016_setPayload(self):
        # Correct (list, None)
        tiipMessage = TIIPMessage()
        tiipMessage.pl = self.payload
        self.assertEqual(tiipMessage.pl, self.payload)
        tiipMessage.pl = None
        self.assertEqual(tiipMessage.pl, None)

        # Incorrect
        with self.assertRaises(TypeError):
            tiipMessage.pl = 1

    def test017_setOk(self):
        # Correct (bool, None)
        tiipMessage = TIIPMessage()
        tiipMessage.ok = self.ok
        self.assertEqual(tiipMessage.ok, self.ok)
        tiipMessage.ok = None
        self.assertEqual(tiipMessage.ok, None)

        # Incorrect
        with self.assertRaises(TypeError):
            tiipMessage.ok = 1

    def test018_setTenant(self):
        # Correct (str, unicode, None)
        tiipMessage = TIIPMessage()
        tiipMessage.ten = str(self.tenant)
        self.assertEqual(tiipMessage.ten, self.tenant)
        tiipMessage.ten = self.tenant
        self.assertEqual(tiipMessage.ten, self.tenant)
        tiipMessage.ten = None
        self.assertEqual(tiipMessage.ten, None)

        # Incorrect
        with self.assertRaises(TypeError):
            tiipMessage.ten = 1

    def test019_strCast(self):
        tiipMessage = self.generateExampleTIIPMessage()
        self.assertEqual(json.loads(str(tiipMessage)), dict(self.tiipDict, pv=self.tiipVersion))

    def test020_dictCast(self):
        tiipMessage = self.generateExampleTIIPMessage()
        self.assertEqual(dict(tiipMessage), dict(self.tiipDict, pv=self.tiipVersion))

    def test021_setChannel(self):
        # Correct (str, unicode, None)
        tiipMessage = TIIPMessage()
        tiipMessage.ch = str(self.channel)
        self.assertEqual(tiipMessage.ch, self.channel)
        tiipMessage.ch = self.channel
        self.assertEqual(tiipMessage.ch, self.channel)
        tiipMessage.ch = None
        self.assertEqual(tiipMessage.ch, None)

        # Incorrect
        with self.assertRaises(TypeError):
            tiipMessage.sig = 1

    def test022_asVersion(self):
        # Correct (str, unicode, None)
        tiipMessage = TIIPMessage()
        tiipMessage.lat = 1.0
        asVersionString = tiipMessage.asVersion("tiip.3.0")
        self.assertEqual(asVersionString, str(tiipMessage))

        asVersionString = tiipMessage.asVersion("tiip.2.0")
        tiip2Dict = json.loads(asVersionString)
        self.assertIn("ct", tiip2Dict.keys())
        self.assertIn("ts", tiip2Dict.keys())
        self.assertIn("pv", tiip2Dict.keys())
        self.assertEqual(tiip2Dict["pv"], "tiip.2.0")
        self.assertAlmostEqual(float(tiip2Dict["ts"]), float(tiip2Dict["ct"]) + 1.0, 5)

    def test023_fromTIIP2(self):
        # Correct (str, unicode, None)
        tiip2String = '{"pv": "tiip.2.0", "ts": "1556099778.77", "ct": "1556099734.255"}'
        tiipMessage = TIIPMessage(tiip2String, verifyVersion=False)
        self.assertAlmostEqual(float(tiipMessage.lat), 44.514999866485596, 5)
        self.assertAlmostEqual(parser.parse(tiipMessage.ts).timestamp(), 1556099734.255, 5)


if __name__ == "__main__":
    unittest.main()
