from telegram import InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardMarkup,KeyboardButton,ParseMode
import emoji
from basket.constants import Constants

class BasketView:

    def __init__(self, index, price = 1000, currency = " тг", count = 1, optional_detail = "", optional_buttons = []):

        self.index                                      = index
        self.price                                      = price
        self.currency                                   = currency
        # number of selected dishes of this type
        self.count                                      = count
        self.first_view                                 = [InlineKeyboardButton("Корзина", callback_data=f"inital_options_{self.index}")]
        self.static_view                                = f'<b>{Constants.BURGER_NAME.value}</b>\n<i>{Constants.INGREDIENTS.value}</i>\nЦена: {Constants.PRICE.value} {Constants.CURRENCY.value}\n{Constants.BURGER_URL.value}'
        self.optional_detail                            = optional_detail
        self.optional_buttons                           = optional_buttons

        self.options_view = [
            InlineKeyboardButton("X", callback_data=f"{self.optional_detail}switch_to_inital_state_{self.index}",  resize_keyboard=True),
            InlineKeyboardButton("1 шт.", callback_data=f"no_reaction_{self.index}",  resize_keyboard=True),
            InlineKeyboardButton("^", callback_data=f"{self.optional_detail}one_more_{self.index}",  resize_keyboard=True)
        ]

    def show_basket_label(self, update, context, is_first_time = False):
        chat_id = update.message.chat.id
        message_id = update.message.message_id
        reply_markup = InlineKeyboardMarkup(self.build_basket_options(self.first_view, n_cols=1))

        if is_first_time:
            context.bot.send_message(
                chat_id = chat_id, 
                text = self.static_view, 
                reply_markup=reply_markup, 
                parse_mode= ParseMode.HTML
                )
        else:
            context.bot.edit_message_text(
                chat_id = chat_id, 
                text = self.static_view, 
                message_id = message_id, 
                reply_markup=reply_markup, 
                parse_mode= ParseMode.HTML
                )

    def show_basket_options(self, update, context, optional_num_buttons = 0, is_first_time = False): 
        chat_id = update.message.chat.id
        message_id = update.message.message_id
        n_cols = 3 if len(self.options_view) == 3 else 4


        reply_markup = InlineKeyboardMarkup(self.build_basket_options(self.options_view, n_cols=n_cols))
        
        if is_first_time:
            context.bot.send_message(
                chat_id = chat_id, 
                text = self.static_view, 
                message_id = message_id, 
                reply_markup=reply_markup, 
                parse_mode= ParseMode.HTML
                )
        else:
            context.bot.edit_message_text(
                chat_id = chat_id, 
                text = self.static_view, 
                message_id = message_id, 
                reply_markup=reply_markup, 
                parse_mode= ParseMode.HTML
                )

    def generate_options_view(self, num = 1, debug_print = False):

        if debug_print: 
            print("inside of generate options view")
            print(num)
            print("*"*30)
        
        self.options_view = [
            InlineKeyboardButton("X", callback_data=f"{self.optional_detail}switch_to_inital_state_{self.index}",  resize_keyboard=True),
            InlineKeyboardButton("-", callback_data=f"{self.optional_detail}one_less_{self.index}",  resize_keyboard=True),
            InlineKeyboardButton(f"{num} шт.", callback_data=f"no_reaction_{self.index}",  resize_keyboard=True),
            InlineKeyboardButton("+", callback_data=f"{self.optional_detail}one_more_{self.index}",  resize_keyboard=True)
        ]

        # adding optional buttons
        if len(self.optional_buttons) > 0:
            for additional_button in self.optional_buttons: 
                self.options_view.append(additional_button)

        if (num == 1):
            del self.options_view[1]
        

    def build_basket_options(self, buttons, n_cols = 1, header_buttons=None, footer_buttons=None):
        menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
        if header_buttons:
            menu.insert(0, [header_buttons])
        if footer_buttons:
            menu.append([footer_buttons])
        return menu