from aiogram.types import InlineKeyboardMarkup as ikm, InlineKeyboardButton as ikb

menu = ikm(inline_keyboard=[
    [ikb(text='SpeechRecognition', callback_data='sr_state')], 
    [ikb(text='SpeechFlow', callback_data='sf_state')],
    [ikb(text='ИНФО >>', callback_data='info')]
    ])

back_menu = ikm(inline_keyboard=[
    [ikb(text='<< Назад', callback_data='back')]
    ])