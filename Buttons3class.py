from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


kisl = InlineKeyboardButton(text='Кислород', callback_data='kisl')
gaz = InlineKeyboardButton(text='Углекислый газ', callback_data='gaz')
azot = InlineKeyboardButton(text='Азот', callback_data='azot')
cl3answ1 = InlineKeyboardMarkup(inline_keyboard=[[kisl], [gaz], [azot]])


morning = InlineKeyboardButton(text='утренняя зарядка', callback_data='morning')
games = InlineKeyboardButton(text='игры на свежем воздухе', callback_data='games')
tv = InlineKeyboardButton(text='долгий просмотр телевизора', callback_data='tv')
pe = InlineKeyboardButton(text='занятия физкультурой.', callback_data='pe')
cl3answ2 = InlineKeyboardMarkup(inline_keyboard=[[morning], [games], [tv], [pe]])


chisl = InlineKeyboardButton(text='числительное', callback_data='chil')
pris = InlineKeyboardButton(text='приставка', callback_data='pris')
chast = InlineKeyboardButton(text='частица', callback_data='chast')
pred = InlineKeyboardButton(text='предлог.', callback_data='pred')
cl3answ3 = InlineKeyboardMarkup(inline_keyboard=[[chisl, pris], [chast, pred]])


s8 = InlineKeyboardButton(text='8', callback_data='s18')
s18 = InlineKeyboardButton(text='18', callback_data='s18')
s80 = InlineKeyboardButton(text='80', callback_data='s80')
s800 = InlineKeyboardButton(text='800', callback_data='s800')
cl3answ5 = InlineKeyboardMarkup(inline_keyboard=[[s8, s18], [s80, s800]])


today = InlineKeyboardButton(text='что можешь сделать сегодня', callback_data='today')
batter = InlineKeyboardButton(text='а две лучше', callback_data='batter')
mind = InlineKeyboardButton(text='зеркало души', callback_data='mind')
next = InlineKeyboardButton(text='дальше будешь', callback_data='next')
cl3answ7 = InlineKeyboardMarkup(inline_keyboard=[[today, batter], [mind, next]])


wthr = InlineKeyboardButton(text='Какая погода будет завтра?', callback_data='wthr')
gold = InlineKeyboardButton(text='Золотые листья кружатся,\n летят и падают на землю.', callback_data='gold')
may = InlineKeyboardButton(text='Сегодня двадцатое мая?', callback_data='may')
happy = InlineKeyboardButton(text='Ты любишь яблоки?', callback_data='happy')
cl3answ8 = InlineKeyboardMarkup(inline_keyboard=[[wthr], [gold], [may], [happy]])


s283 = InlineKeyboardButton(text='283', callback_data='s283')
s192 = InlineKeyboardButton(text='192', callback_data='s192')
s90 = InlineKeyboardButton(text='90', callback_data='s90')
s219 = InlineKeyboardButton(text='219', callback_data='s219')
cl3answ9 = InlineKeyboardMarkup(inline_keyboard=[[s283, s192], [s90, s219]])


moh = InlineKeyboardButton(text='мхи', callback_data='moh')
vodor = InlineKeyboardButton(text='водоросли', callback_data='vodor')
paporotnik = InlineKeyboardButton(text='папоротники', callback_data='paporotnik')
berez = InlineKeyboardButton(text='березы', callback_data='berez')
cl3answ10 = InlineKeyboardMarkup(inline_keyboard=[[moh, vodor], [paporotnik, berez]])


poh = InlineKeyboardButton(text='поход', callback_data='poh')
posud = InlineKeyboardButton(text='посуда', callback_data='posud')
flour = InlineKeyboardButton(text='пол ', callback_data='flour')
poni = InlineKeyboardButton(text='пони', callback_data='poni')
cl3answ12 = InlineKeyboardMarkup(inline_keyboard=[[poh, posud], [flour, poni]])