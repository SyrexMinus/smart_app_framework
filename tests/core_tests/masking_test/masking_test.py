from unittest import TestCase

import json
from core.message.from_message import SmartAppFromMessage


class MaskingTest(TestCase):
    def test_1(self):
        input_msg = {
            "messageId": 2,
            "uuid": {"userChannel": "B2C", "userId": "userId", "sub": "sub"},
            "payload": {
                "message": {
                    "original_text": "Номер карты 1234567890123456"
                }
            },
            "messageName": "MESSAGE_TO_SKILL"
        }

        json_input_msg = json.dumps(input_msg, ensure_ascii=False)
        message = SmartAppFromMessage(value=json_input_msg, headers=[])

        masked_message = json.loads(message.masked_value)

        self.assertEqual(masked_message['payload']['message']['original_text'], "Номер карты ************3456")

    def test_2(self):
        input_msg = {
            "messageId": 2,
            "uuid": {"userChannel": "B2C", "userId": "userId", "sub": "sub"},
            "payload": {
                "message": {
                    "original_text": "Номер карты 1234567890123456 вот"
                }
            },
            "messageName": "MESSAGE_TO_SKILL"
        }

        json_input_msg = json.dumps(input_msg, ensure_ascii=False)
        message = SmartAppFromMessage(value=json_input_msg, headers=[])

        masked_message = json.loads(message.masked_value)

        self.assertEqual(masked_message['payload']['message']['original_text'], "Номер карты ************3456 вот")

    def test_3(self):
        input_msg = {
            "messageId": 2,
            "uuid": {"userChannel": "B2C", "userId": "userId", "sub": "sub"},
            "payload": {
                "message": {
                    "original_text": "Номер карты1234567890123456 вот"
                }
            },
            "messageName": "MESSAGE_TO_SKILL"
        }

        json_input_msg = json.dumps(input_msg, ensure_ascii=False)
        message = SmartAppFromMessage(value=json_input_msg, headers=[])

        masked_message = json.loads(message.masked_value)

        self.assertEqual(masked_message['payload']['message']['original_text'], "Номер карты************3456 вот")

    def test_4(self):
        input_msg = {
            'token': [12, 12, {'key': [12, 12]}],
            'notoken': [12, {'token': 12}]
        }
        json_input_msg = json.dumps(input_msg, ensure_ascii=False)
        message = SmartAppFromMessage(value=json_input_msg, headers=[])

        masked_message = json.loads(message.masked_value)
        result_message = {'token': ['***', '***', {'key': '*items-2*collections-0*maxdepth-1*'}], 'notoken': [12, {'token': '***'}]}

        self.assertEqual(masked_message, result_message)

    def test_5(self):
        input_msg = {
            "messageId": 2,
            "uuid": {"userChannel": "B2C", "epkId": "epkId", "sub": "sub"},
            "payload": {
                "message": {
                    "original_text": "Номер карты1234567890123456 вот"
                },
                "profileId":[123, 456]
            },
            "messageName": "MESSAGE_TO_SKILL",
            "data" :{
                "refresh_token": [123, 456, {"key": {"inner_dict" : ["inner_list", 123, 456]}}]
            }
        }

        json_input_msg = json.dumps(input_msg, ensure_ascii=False)
        message = SmartAppFromMessage(value=json_input_msg, headers=[])

        masked_message = json.loads(message.masked_value)
        result_message = input_msg = {
            "messageId": 2,
            "uuid": {"userChannel": "B2C", "epkId": "***", "sub": "sub"},
            "payload": {
                "message": {
                    "original_text": "Номер карты************3456 вот"
                },
                "profileId":['***', '***']
            },
            "messageName": "MESSAGE_TO_SKILL",
            "data" :{
                "refresh_token": ['***', '***', {'key': '*items-3*collections-1*maxdepth-2*'}]
            }
        }

        self.assertEqual(masked_message, result_message)