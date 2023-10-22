'''class Message:
    def __init__(self, currency, total_amount, invoice_payload, shipping_option_id, order_info,
                 telegram_payment_charge_id, provider_payment_charge_id):
        self.currency = currency
        self.total_amount = total_amount
        self.invoice_payload = invoice_payload
        self.shipping_option_id = shipping_option_id
        self.order_info = order_info
        self.telegram_payment_charge_id = telegram_payment_charge_id
        self.provider_payment_charge_id = provider_payment_charge_id'''

from main import bot
class Message:
    def __init__(self, message):
        self.bot = bot  # Объект платежной системы
        self.chat_id = message['chat']['id']  # Объект платежной системы
        self.user_id = message['user']['id']  # id пользователя в телеграмме
        self.message_id = message['message_id']  # id транзакции
        self.direction = 'incoming'# не разобралась с возвратом
        self.title = message['invoice']['id']
        self.payload = message['SuccessfulPayment']['invoice_payload']
        self.content_type = 'payment'  # только "payment"
        self.content = message['createInvoiceLink']['provider_data']  # str с JSON с информацией о транзации
        self.username = message['user']['username']  # username в телеграме или "Not avalible"