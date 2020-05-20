from telegram import InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardMarkup,KeyboardButton,ParseMode


class BasketMenuView(): 
    """
    TestView class:
        the main responsibility of this class is 'sending messages of each state in bot'
        and also 'formatting of messages', etc.
    """
    
    def __init__(self, title):
        self.title = title
        self.custom_keyboard = [[KeyboardButton('Начало'), KeyboardButton('Корзина')], 
                   [            KeyboardButton('Меню')]]
    
    def send_price_details(self, update, context, price_details = "100 тг"):
        chat_id = update.message.chat.id
        context.bot.send_message(chat_id=chat_id, text=f"<b>{price_details}</b>", parse_mode= ParseMode.HTML)

    def show_keyboard_menu(self, update, context, text = ""):
        chat_id = update.message.chat.id

        reply_markup = ReplyKeyboardMarkup(self.custom_keyboard, resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=chat_id, 
                        text=text, 
                        reply_markup=reply_markup)
