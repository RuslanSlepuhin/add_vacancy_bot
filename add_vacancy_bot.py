import os
from datetime import datetime

import aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
import configparser
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
import psycopg2

config = configparser.ConfigParser()
config.read("./settings/config.ini")

token = os.getenv('token')
database = os.getenv('database')
user = os.getenv('user')
password = os.getenv('password')
host = os.getenv('host')
port = os.getenv('port')
#
# token = config['Token']['token']
# database = config['DB']['database']
# user = config['DB']['user']
# password = config['DB']['password']
# host = config['DB']['host']
# port = config['DB']['port']

logging.basicConfig(level=logging.INFO)
bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class AddVacancy:
    def __init__(self):
        self.history_messages = []
        self.markup = None

    def main_self(self):

        @dp.message_handler(commands=['start'])
        async def send_welcome(message: types.Message):
            self.markup = ReplyKeyboardMarkup(row_width=4, resize_keyboard=True)
            button = KeyboardButton('To send the vacancy')
            self.markup.add(button)

            self.history_messages.append(await bot.send_message(message.chat.id, 'It asks you to full 11 fields like:\n'
                                                    '<b>-source</b> - is the vacancy from\n'
                                                    '<b>-vacancy</b> - the vacancy name\n'
                                                    '<b>-professions</b> - the list of professions\n'
                                                    '<b>-company</b>\n'
                                                    '<b>-english</b>\n'
                                                    '<b>-relocation</b>\n'
                                                    '<b>-job_type</b>\n'
                                                    '<b>-city</b>\n'
                                                    '<b>-salary</b>\n'
                                                    '<b>-experience</b>\n'
                                                    '<b>-contacts</b>\n'
                                                    '<b>-body</b> - the vacancy description\n\n'
                                                    'feel free to skip any step to type *\n\n'
                                                    'Let start', parse_mode='html', reply_markup=self.markup)
                                         )

        class Form_vacancy(StatesGroup):
            source = State()
            vacancy = State()
            professions = State()
            company = State()
            english = State()
            relocation = State()
            job_type = State()
            city = State()
            salary = State()
            experience = State()
            contacts = State()
            body = State()

        # Возможность отмены, если пользователь передумал заполнять
        @dp.message_handler(state='*', commands=['cancel', 'start'])
        @dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
        async def cancel_handler(message: types.Message, state: FSMContext):
            current_state = await state.get_state()
            if current_state is None:
                return

            await state.finish()
            await message.reply('You need to press the /start for start again')

        @dp.message_handler(state=Form_vacancy.source)
        async def process_phone_number(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['source'] = ''
                if message.text != "*":
                    data['source'] = message.text
                await Form_vacancy.next()
                await bot.send_message(message.chat.id, 'Type the vacancy name /cancel', parse_mode='html')

        @dp.message_handler(state=Form_vacancy.vacancy)
        async def process_phone_number(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['vacancy'] = ''
                if message.text != "*":
                    data['vacancy'] = message.text
                await Form_vacancy.next()
                await bot.send_message(message.chat.id, "Type several professions trow ', ' /cancel", parse_mode='html')

        @dp.message_handler(state=Form_vacancy.professions)
        async def process_phone_number(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['professions'] = ''
                if message.text != "*":
                    data['professions'] = message.text
                await Form_vacancy.next()
                await bot.send_message(message.chat.id, "Type the company name /cancel", parse_mode='html')

        @dp.message_handler(state=Form_vacancy.company)
        async def process_phone_number(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['company'] = ''
                if message.text != "*":
                    data['company'] = message.text
                await Form_vacancy.next()
                await bot.send_message(message.chat.id, "Type the english level /cancel", parse_mode='html')

        @dp.message_handler(state=Form_vacancy.english)
        async def process_phone_number(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['english'] = ''
                if message.text != "*":
                    data['english'] = message.text
                await Form_vacancy.next()
                await bot.send_message(message.chat.id, "Type the requirements of relocation /cancel", parse_mode='html')

        @dp.message_handler(state=Form_vacancy.relocation)
        async def process_phone_number(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['relocation'] = ''
                if message.text != "*":
                    data['relocation'] = message.text
                await Form_vacancy.next()
                await bot.send_message(message.chat.id, "Type the describes of job type /cancel", parse_mode='html')

        @dp.message_handler(state=Form_vacancy.job_type)
        async def process_phone_number(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['job_type'] = ''
                if message.text != "*":
                    data['job_type'] = message.text
                await Form_vacancy.next()
                await bot.send_message(message.chat.id, "Type the vacancy city /cancel", parse_mode='html')

        @dp.message_handler(state=Form_vacancy.city)
        async def process_phone_number(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['city'] = ''
                if message.text != "*":
                    data['city'] = message.text
                await Form_vacancy.next()
                await bot.send_message(message.chat.id, "Type the salary /cancel", parse_mode='html')

        @dp.message_handler(state=Form_vacancy.salary)
        async def process_phone_number(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['salary'] = ''
                if message.text != "*":
                    data['salary'] = message.text
                await Form_vacancy.next()
                await bot.send_message(message.chat.id, "Type the experience /cancel", parse_mode='html')

        @dp.message_handler(state=Form_vacancy.experience)
        async def process_phone_number(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['experience'] = ''
                if message.text != "*":
                    data['experience'] = message.text
                await Form_vacancy.next()
                await bot.send_message(message.chat.id, "Type the contacts /cancel", parse_mode='html')

        @dp.message_handler(state=Form_vacancy.contacts)
        async def process_phone_number(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['contacts'] = ''
                if message.text != "*":
                    data['contacts'] = message.text
                await Form_vacancy.next()
                await bot.send_message(message.chat.id, "Type the vacancy body /cancel", parse_mode='html')

        @dp.message_handler(state=Form_vacancy.body)
        async def process_phone_number(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['body'] = ''
                if message.text != "*":
                    data['body'] = message.text
                await print_info(message, data)
                await state.finish()

        @dp.message_handler(content_types=['text'])
        async def messages(message):
            if message.text == 'To send the vacancy':
                await delete_messages()
                await Form_vacancy.source.set()
                await bot.send_message(message.chat.id, 'Type the <b>source</b> the vacancy from', parse_mode='html')
            else:
                await bot.delete_message(message.chat.id, message.message_id)


        async def print_info(message, data):
            message_for_send = ''
            for i in data:
                if data[i]:
                    message_for_send += f"{i}: {data[i]}\n"

            if message_for_send:
                await bot.send_message(message.chat.id, message_for_send)
                await push_to_admin_table(message, message_for_send, data)

            else:
                await bot.send_message(message.chat.id, "<b>Hey, message is empty!</b>\nPress button to do it again",
                                       parse_mode='html', reply_markup=self.markup)



        async def push_to_admin_table(message, message_for_send, data):

            con = psycopg2.connect(
                database=database,
                user=user,
                password=password,
                host=host,
                port=port
            )
            vacancy = data['vacancy']
            cur = con.cursor()
            new_post = f"""INSERT INTO admin_last_session (
                                    chat_name, title, body, profession, vacancy, company, english, relocation, job_type, 
                                    city, salary, experience, contacts, time_of_public, created_at) 
                                                VALUES ('{data['source']}', '{data['vacancy']}', '{message_for_send}', 
                                                '{data['professions']}', '{data['vacancy']}', '{data['company']}', 
                                                '{data['english']}', '{data['relocation']}', '{data['job_type']}', 
                                                '{data['city']}', '{data['salary']}', '{data['experience']}', 
                                                '{data['contacts']}', '{datetime.now()}', '{datetime.now()}');"""
            #
            # source = State()
            # vacancy = State()
            # professions = State()
            # company = State()
            # english = State()
            # relocation = State()
            # job_type = State()
            # city = State()
            # salary = State()
            # experience = State()
            # contacts = State()
            # body = State()

            with con:
                try:
                    cur.execute(new_post)
                    await bot.send_message(message.chat.id, 'This vacancy has been added to admin',
                                           reply_markup=self.markup)
                except Exception as e:
                    await bot.send_message(message.chat.id, f'There is some problems: {e}')

        async def delete_messages():
            for i in self.history_messages:
                await i.delete()


        executor.start_polling(dp, skip_updates=True)

AddVacancy().main_self()