from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from texts import *
import app.keyboards as kb
from app.handlers import Crypt
from aiogram import F, Router

call_router = Router()

@call_router.callback_query(F.data == 'info')
async def info(callback: CallbackQuery):
    await callback.message.edit_text(INFO_TEXT, reply_markup=kb.back_menu)

@call_router.callback_query(F.data == 'back')
async def info(callback: CallbackQuery):
    await callback.message.edit_text(MAIN_TEXT(callback.from_user.first_name), reply_markup=kb.menu)

@call_router.callback_query(F.data == 'sr_state')
async def choose_sr_state(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Crypt.speechrecognition_state)
    await callback.message.edit_text(SEND_AUDIO_OR_VOICE(callback.from_user.first_name), reply_markup=kb.back_menu)

@call_router.callback_query(F.data == 'sf_state')
async def choose_sr_state(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Crypt.speechflow_state)
    await callback.message.edit_text(SEND_AUDIO_OR_VOICE(callback.from_user.first_name), reply_markup=kb.back_menu)
