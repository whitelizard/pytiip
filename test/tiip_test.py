import json
import unittest

from pytiip.tiip import TIIPMessage


class TestTIIPMessage(unittest.TestCase):

    def __init__(self, methodName='runTest'):
        unittest.TestCase.__init__(self, methodName)

        # Key examples
        self.timestamp = '123456789.123'
        self.clientTime = '987654321.987'
        self.mid = 'testMid'
        self.sid = 'testSid'
        self.type = 'testType'
        self.source = ['testSource1', 'testSource2']
        self.pid = 'testPid'
        self.target = 'testTarget'
        self.subTarget = 'testSubTarget'
        self.signal = 'testSignal'
        self.arguments = {'testArgument1': 'testArgumentValue1', 'testArgument2': 'testArgumentValue2'}
        self.payload = ['testPayloadValue1', 'testPayloadValue2']
        self.ok = True
        self.tenant = 'testTenant'

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
        tiipMsg = TIIPMessage(timestamp=self.timestamp, clientTime=self.clientTime, mid=self.mid, sid=self.sid,
                              type=self.type, source=self.source, pid=self.pid, target=self.target, subTarget=self.subTarget,
                              signal=self.signal, arguments=self.arguments, payload=self.payload, ok=self.ok, tenant=self.tenant)
        self.verifyKeys(tiipMsg)

    def test001_initFromDict(self):
        tiipMsg = TIIPMessage(tiipDict=self.tiipDict)
        self.verifyKeys(tiipMsg)

    def test002_initFromStr(self):
        tiipMsg = TIIPMessage(tiipStr=self.tiipStr)
        self.verifyKeys(tiipMsg)

if __name__ == "__main__":
    unittest.main()
