from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputFile


gus = InlineKeyboardButton(text='«Гуси-лебеди»', callback_data='gus')
col = InlineKeyboardButton(text='«Колобок»', callback_data='col')
strah = InlineKeyboardButton(text='«У страха глаза велики»', callback_data='strah')
kasha = InlineKeyboardButton(text='«Каша из топора»', callback_data='kasha')
cl2answ1 = InlineKeyboardMarkup(inline_keyboard=[[gus, col], [strah, kasha]])


gr1 = InlineKeyboardButton(text='лев, львёнок, левый, \nльвиный  ', callback_data='gr1')
gr2 = InlineKeyboardButton(text='соль, солнечный, солёный,\n посолить  ', callback_data='gr2')
gr3 = InlineKeyboardButton(text='добро, добрый, доброта,\n подобреть  ', callback_data='gr3')
gr4 = InlineKeyboardButton(text='лиса, лисичка, листик, \nлисонька', callback_data='gr4')
cl2answ2 = InlineKeyboardMarkup(inline_keyboard=[[gr1], [gr2], [gr3], [gr4]])

s61 = InlineKeyboardButton(text='61', callback_data='s61')
s71 = InlineKeyboardButton(text='71', callback_data='s71')
s59 = InlineKeyboardButton(text='59', callback_data='s59')
s44 = InlineKeyboardButton(text='44', callback_data='s44')
cl2answ3 = InlineKeyboardMarkup(inline_keyboard=[[s61, s71], [s59, s44]])


ecr = InlineKeyboardButton(text='экран, медуза, жираф, юбка', callback_data='ecr')
ded = InlineKeyboardButton(text='дедушка, щавель, этажи, хорёк', callback_data='ded')
ruk = InlineKeyboardButton(text='рюкзак, йод, циклон, веревка', callback_data='ruk')
chudo = InlineKeyboardButton(text='чудо, льдинка, иголка, фамилия', callback_data='chudo')
cl2answ4 = InlineKeyboardMarkup(inline_keyboard=[[ecr], [ded], [ruk], [chudo]])


kar = InlineKeyboardButton(text='Карандаш, краски, лампа', callback_data='kar')
snow = InlineKeyboardButton(text='Снег, дождь, иней', callback_data='snow')
rust = InlineKeyboardButton(text='Растения, человек, животные.', callback_data='rust')
cl2answ5 = InlineKeyboardMarkup(inline_keyboard=[[kar], [snow], [rust]])


tap = InlineKeyboardButton(text='тапочки', callback_data='tap')
socks = InlineKeyboardButton(text='носки', callback_data='socks')
perch = InlineKeyboardButton(text='перчатки', callback_data='perch')
chair = InlineKeyboardButton(text='ножки стула', callback_data='chair')
cl2answ6 = InlineKeyboardMarkup(inline_keyboard=[[tap], [socks], [perch], [chair]])


sqwr = InlineKeyboardButton(text='Квадрат', callback_data='sqwr')
rect = InlineKeyboardButton(text='Прямоугольник', callback_data='rect')
trngl = InlineKeyboardButton(text='Треугольник', callback_data='trngl')
romb = InlineKeyboardButton(text='Ромб', callback_data='romb')
cl2answ8 = InlineKeyboardMarkup(inline_keyboard=[[sqwr, rect], [trngl, romb]])


s01 = InlineKeyboardButton(text='01', callback_data='s01')
s02 = InlineKeyboardButton(text='02', callback_data='s02')
s03 = InlineKeyboardButton(text='03', callback_data='s03')
s04 = InlineKeyboardButton(text='04', callback_data='s04')
cl2answ9 = InlineKeyboardMarkup(inline_keyboard=[[s01, s02], [s03, s04]])


green = InlineKeyboardButton(text='зеленый', callback_data='green')
yellow = InlineKeyboardButton(text='желтый', callback_data='yellow')
red = InlineKeyboardButton(text='красный', callback_data='red')
cl2answ10 = InlineKeyboardMarkup(inline_keyboard=[[green], [yellow], [red]])
