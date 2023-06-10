from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputFile


a11 = InlineKeyboardButton(text='маяк', callback_data='a11')
a12 = InlineKeyboardButton(text='январь', callback_data='a12')
a13 = InlineKeyboardButton(text='осина', callback_data='a13')
a14 = InlineKeyboardButton(text='уголь', callback_data='a14')
cl1answ1 = InlineKeyboardMarkup(inline_keyboard=[[a11, a12], [a13, a14]])

a21 = InlineKeyboardButton(text='13 и 15', callback_data='a21')
a22 = InlineKeyboardButton(text='16 и 18', callback_data='a22')
a23 = InlineKeyboardButton(text='12 и 14', callback_data='a23')
a24 = InlineKeyboardButton(text='14 и 18', callback_data='a24')
cl1answ2 = InlineKeyboardMarkup(inline_keyboard=[[a21, a22], [a23, a24]])

st = InlineKeyboardButton(text='Санкт-Петербург', callback_data='st')
mos = InlineKeyboardButton(text='Москва', callback_data='mos')
nov = InlineKeyboardButton(text='Новгород', callback_data='nov')
kal = InlineKeyboardButton(text='Калининград', callback_data='kal')
cl1answ3 = InlineKeyboardMarkup(inline_keyboard=[[st, mos], [nov, kal]])

a41 = InlineKeyboardButton(text='ноготь', callback_data='a41')
a42 = InlineKeyboardButton(text='нос', callback_data='a42')
a43 = InlineKeyboardButton(text='кожа ', callback_data='a43')
a44 = InlineKeyboardButton(text='язык', callback_data='a44')
cl1answ4 = InlineKeyboardMarkup(inline_keyboard=[[a41, a42], [a43, a44]])

a51 = InlineKeyboardButton(text='плачет', callback_data='a51')
a52 = InlineKeyboardButton(text='плоды', callback_data='a52')
a53 = InlineKeyboardButton(text='хороший', callback_data='a53')
a54 = InlineKeyboardButton(text='холодно', callback_data='a53')
cl1answ5 = InlineKeyboardMarkup(inline_keyboard=[[a51, a52], [a53, a54]])


a61 = InlineKeyboardButton(text='осенью', callback_data='a61')
a62 = InlineKeyboardButton(text='весной', callback_data='a62')
a63 = InlineKeyboardButton(text='летом', callback_data='a63')
a64 = InlineKeyboardButton(text='зимой', callback_data='a64')
cl1answ6 = InlineKeyboardMarkup(inline_keyboard=[[a61, a62], [a63, a64]])


a81 = InlineKeyboardButton(text='п_льто', callback_data='a81')
a82 = InlineKeyboardButton(text='м_лина', callback_data='a82')
a83 = InlineKeyboardButton(text='в_рона', callback_data='a83')
a84 = InlineKeyboardButton(text='м_шина', callback_data='a84')
cl1answ8 = InlineKeyboardMarkup(inline_keyboard=[[a81, a82], [a83, a84]])

a101 = InlineKeyboardButton(text='Пословица', callback_data='a101')
a102 = InlineKeyboardButton(text='сказка', callback_data='a102')
a103 = InlineKeyboardButton(text='загадка', callback_data='a103')
a104 = InlineKeyboardButton(text='рассказ', callback_data='a104')
a105 = InlineKeyboardButton(text='запятая', callback_data='a105')
cl1answ10 = InlineKeyboardMarkup(inline_keyboard=[[a101, a102], [a103, a104, a105]])
