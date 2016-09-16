# -*- coding: utf-8 -*-
'''
    :codeauthor: :email:`Jayesh Kariya <jayeshk@saltstack.com>`
'''
# Import Python libs
from __future__ import absolute_import

# Import Salt Testing Libs
from salttesting import skipIf, TestCase
from salttesting.mock import (
    NO_MOCK,
    NO_MOCK_REASON,
    MagicMock,
    patch)

from salttesting.helpers import ensure_in_syspath

ensure_in_syspath('../../')

# Import Salt Libs
from salt.engines import sqs_events

sqs_events.__salt__ = {}
sqs_events.__opts__ = {}


@skipIf(NO_MOCK, NO_MOCK_REASON)
class EngineSqsEventTestCase(TestCase):
    '''
    Test cases for salt.engine.sqs_events
    '''
    # 'present' function tests: 1
    @patch('salt.engines.sqs_events.log')
    @patch('time.sleep', return_value=None)
    def test_no_queue_presenet(self, mock_sleep, mock_logging):
        '''
        Test to ensure the SQS engine starts.
        '''
        q = None
        q_name = 'mysqs'
        sqs_events._process_queue(q, q_name)
        self.assertTrue(mock_logging.warning.called)


if __name__ == '__main__':
    from integration import run_tests
    run_tests(EngineSqsEventTestCase, needs_daemon=False)
