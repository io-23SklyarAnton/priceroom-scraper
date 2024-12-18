import json
from io import BytesIO
import telebot
import time
from collections import defaultdict
import platform
import utils
if not platform.system() == 'Linux':
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context


class Notification:
    def __init__(self):
        self.telegram_bot = telebot.TeleBot(utils.TELEGRAM_TOKEN)
        self.last_notifications = defaultdict(float)
        self.notification_frequency = 30.0

    def telegram(
            self,
            message='',
            _type='INFO',
            data=None,
            users=utils.TELEGRAM_USERS_TO_NOTIFY,
    ):
        _type = '[' + _type + ']\n'
        for user_id in users:
            try:
                self.telegram_bot.send_message(user_id, f'{_type} {message}')

                if data:
                    data_json = json.dumps(data, indent=4)
                    data_bytes = data_json.encode('utf-8')
                    data_stream = BytesIO(data_bytes)
                    data_stream.name = 'data.json'

                    self.telegram_bot.send_document(user_id, data_stream)
            except:
                continue

    def __frequency_limit(self, message):
        current_time = time.time()
        if not self.last_notifications.get(message):
            self.last_notifications[message] = current_time
            return True

        if current_time - self.last_notifications.get(message) >= self.notification_frequency:
            self.last_notifications[message] = current_time
            return True
