from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class CurrenciesConsumer(WebsocketConsumer):
    def connect(self):
        # Connect channel with name 'self.channel_name'
        # to 'currencies' group
        async_to_sync(self.channel_layer.group_add)(
            "currencies", self.channel_name
        )
        # Get connection
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            "currencies", self.channel_name
        )

    # Method 'currencies_currency' - event handler 'currencies.currency'
    def currencies_currency(self, event):
        # Send message through websocket
        self.send(text_data=event["text"])