import requests
import json

class TelegramBot:
    def __init__(self, token):
        self.token = token
        self.api_url = f"https://api.telegram.org/bot{token}/"

    def get_updates(self, offset=None):
        method = 'getUpdates'
        params = {'timeout': 30, 'offset': offset}
        response = requests.get(self.api_url + method, params)
        result_json = response.json()['result']
        return result_json

    def send_message(self, chat_id, text, reply_markup=None):
        method = 'sendMessage'
        params = {'chat_id': chat_id, 'text': text, 'reply_markup': reply_markup}
        response = requests.post(self.api_url + method, params)
        return response

    def handle_updates(self, updates, print_callback=None):
        for update in updates:
            if 'message' in update:
                message = update['message']
                chat_id = message['chat']['id']

                if 'text' in message:
                    text = message['text']
                    if print_callback:
                        print_callback(chat_id, text, None)
                elif 'photo' in message:
                    photo = message['photo']
                    if print_callback:
                        print_callback(chat_id, photo, None)
                elif 'document' in message:
                    document = message['document']
                    if print_callback:
                        print_callback(chat_id, document, None)

            elif 'callback_query' in update:
                callback_query = update['callback_query']
                chat_id = callback_query['message']['chat']['id']
                query = callback_query['data']
                if print_callback:
                    print_callback(chat_id, None, query)

            # Son işlenen güncelleme ID'sini güncelleme
            last_update_id = update['update_id']
            self.get_updates(offset=last_update_id + 1)



    def inlinekeyboardmarkup(self, buttons):
        keyboard = {'inline_keyboard': buttons}
        return json.dumps(keyboard)

    def inlinekeyboardbutton(self, text, callback_data):
        button = {'text': text, 'callback_data': callback_data}
        return button
