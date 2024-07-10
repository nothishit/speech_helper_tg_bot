import os, subprocess, speech_recognition as sr
from dotenv import load_dotenv
from aiogram import F, Router, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from app.texts import *
from app.speechflow import start_speech_flow
import app.keyboards as kb
from aiogram.fsm.context import FSMContext

load_dotenv()
router = Router()
r = sr.Recognizer()
bot = Bot(token=os.getenv('TOKEN'), default=DefaultBotProperties(parse_mode='HTML'))
ffmpeg_path = os.getenv('FFMPEG_PATH')

class Crypt(StatesGroup):
    speechflow_state = State()
    speechrecognition_state = State()

@router.message(Command('start', 'help'))
async def commands_start(message: Message, state: FSMContext):
    await state.set_state(Crypt.speechrecognition_state)
    await message.answer(WELCOME_TEXT(message.from_user.first_name), reply_markup=kb.menu)

# speechflow
@router.message(F.audio, Crypt.speechflow_state)
async def send_transcrypt_mp3_speech_flow(message: Message):
    split_tup = os.path.splitext(message.audio.file_name)
    file_name = f'{split_tup[0]}_{message.from_user.full_name}{split_tup[1]}'
    await bot.download(message.audio.file_id, file_name)
    
    file_name_wav = f'{split_tup[0]}_{message.from_user.full_name}.wav'
    subprocess.call([ffmpeg_path, '-i', file_name, file_name_wav])

    text = start_speech_flow(file_name_wav)
    await message.answer(SPEECH_FLOW)
    if len(text) <= 4096:
        await message.answer(text)
    else:
        for i in range(len(text)//4096 + 1):
            text_part = text[:4096]
            await message.answer(text_part)
            if len(text) >= 4096:
                text = text[4096:]

    os.remove(file_name)
    os.remove(file_name_wav)

@router.message(F.voice, Crypt.speechflow_state)
async def send_transcrypt_speech_flow(message: Message):
    file_name = f'{message.from_user.full_name}.mp3'
    await bot.download(message.voice.file_id, file_name)
    
    file_name_wav = f'{message.from_user.full_name}.wav'
    subprocess.call([ffmpeg_path, '-i', file_name, file_name_wav])
    
    text = start_speech_flow(file_name_wav)
    await message.answer(SPEECH_FLOW)
    if len(text) <= 4096:
        await message.answer(text)
    else:
        for i in range(len(text)//4096 + 1):
            text_part = text[:4096]
            await message.answer(text_part)
            if len(text) >= 4096:
                text = text[4096:]

    os.remove(file_name)
    os.remove(file_name_wav)

# speech recognition
@router.message(F.audio, Crypt.speechrecognition_state)
async def send_transcrypt_mp3_google_recognition(message: Message):
    split_tup = os.path.splitext(message.audio.file_name)
    file_name = f'{split_tup[0]}_{message.from_user.full_name}{split_tup[1]}'
    await bot.download(message.audio.file_id, file_name)
    
    file_name_wav = f'{split_tup[0]}_{message.from_user.full_name}.wav'
    subprocess.call([ffmpeg_path, '-i', file_name, file_name_wav])

    with sr.AudioFile(file_name_wav) as source:
        audio = r.record(source)
    await message.answer(SPEECH_RECOGNITION)
    try:
        text = r.recognize_google(audio, language="ru")
        await message.answer(text)
    except:
        await message.answer(UNKNOWN_TEXT)

    os.remove(file_name)
    os.remove(file_name_wav)

@router.message(F.voice, Crypt.speechrecognition_state)
async def send_transcrypt_google_recognition(message: Message): 
    file_name = f'{message.from_user.full_name}.mp3'
    await bot.download(message.voice.file_id, file_name)
    
    file_name_wav = f'{message.from_user.full_name}.wav'
    subprocess.call([ffmpeg_path, '-i', file_name, file_name_wav])

    with sr.AudioFile(file_name_wav) as source:
        voice = r.record(source)
    await message.answer(SPEECH_RECOGNITION)
    try:
        text = r.recognize_google(voice, language="ru")
        await message.answer(text)
    except:
        await message.answer(UNKNOWN_TEXT)

    os.remove(file_name)
    os.remove(file_name_wav)