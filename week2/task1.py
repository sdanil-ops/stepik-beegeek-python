#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#
#    displays  "Hello, world!". You can paste any name against 'world'
#    -----------------------------------------------------------
import unittest


class HelloMessage:

    def __init__(self, recipient: str = None):
        if recipient is not None:
            self.recipient = recipient
        else:
            self.recipient = 'мир'

    def __str__(self):
        return f'Здравствуй, {self.recipient}!'

    def __call__(self):
        print(self.__str__())


class TestHelloMessage(unittest.TestCase):

    def test__str__(self):
        test_items = {
            'item 1': HelloMessage('test'),
            'item 2': HelloMessage('python'),
            'item 3': HelloMessage('Гвидо'),
            'item 4': HelloMessage('мир')
        }
        for test_item in test_items:
            self.assertEqual(test_items[test_item].__str__(), f'Здравствуй, {test_items[test_item].recipient}!')


if __name__ == '__main__':
    hello_message = HelloMessage()
    hello_message()
