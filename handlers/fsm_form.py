from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from aiogram.dispatcher.filters.state import StatesGroup, State

from config import bot, DESTINATION_DIR
from database.sql_commands import Database

class FormStates(StatesGroup):
    nickname = State()
    bio = State()
    age = State()
    occupation = State()
    married = State()
    photo = State()

async def fsm_start(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.message.chat.id,
        text="Send me your nickname"
    )
    await FormStates.nickname.set()

async def load_nickname(message: types.Message,
                        state: FSMContext):
    async with state.proxy() as data:
        data['nickname'] = message.text
        print(data)
    await FormStates.next()
    await message.reply(
        "Send me your bio, please"
    )
async def load_bio(message: types.Message,
                   state: FSMContext):
    async with state.proxy() as data:
        data["bio"] = message.text
        print(data)
    await FormStates.next()
    await message.reply(
        "Send me your age, use only numeric text"
    )


async def load_age(message: types.Message,
                   state: FSMContext):
    try:
        if type(int(message.text)) != int:
            await message.reply(
                text="I said use numeric one, register again"
            )
            await state.finish()
        else:
            async with state.proxy() as data:
                data["age"] = message.text
                print(data)
            await FormStates.next()
            await message.reply(
                "Send me your occupation, please"
            )
    except ValueError as e:
        await state.finish()
        await message.reply(
            text="I said use numeric one, register again"
        )

async def load_occupation(message: types.Message,
                   state: FSMContext):
    async with state.proxy() as data:
        data['occupation'] = message.text
        print(data)
    await FormStates.next()
    await message.reply(
        "Are u married, if u dont want to asnwer, send -"
    )

async def load_married(message: types.Message,
                   state: FSMContext):
    async with state.proxy() as data:
        data['bio'] = message.text
        print(data)
    await FormStates.next()
    await message.reply(
        "Send me your photo, use photo not file sending method"
    )

async def load_photo(message: types.Message,
                     state: FSMContext):
    print(message.photo)
    path = await message.photo[-1].download(
        destination_dir=DESTINATION_DIR
    )
    async with state.proxy() as data:
        Database().sql_insert_user_form_command(
            telegram_id=message.from_user.id,
            nickname=data["nickname"],
            bio=data["bio"],
            age=data["age"],
            occupation=data["occupation"],
            married=data["married"],
            photo=path.name,
        )
        await message.reply(text="Registered Successfully")
        await state.finish()
def register_fsm_form_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(fsm_start,
                                       lambda call: call.data == 'fsm_start_form')
    dp.register_message_handler(load_nickname, state=FormStates.nickname,
                                content_types=['text'])
    dp.register_message_handler(load_bio, state=FormStates.bio,
                                content_types=['text'])
    dp.register_message_handler(load_age, state=FormStates.age,
                                content_types=['text'])
    dp.register_message_handler(load_occupation, state=FormStates.occupation,
                                content_types=['text'])
    dp.register_message_handler(load_married, state=FormStates.married,
                                content_types=['text'])
    dp.register_message_handler(load_photo, state=FormStates.photo,
                                content_types=types.ContentTypes.PHOTO)
