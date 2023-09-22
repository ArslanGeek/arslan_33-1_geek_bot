from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

async def start_keyboard():
    makrup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Начать опросник",
        callback_data="start_questionnaire"
    )
    form_start_button = InlineKeyboardButton(
        "Registration",
        callback_data="fsm_start_form"
    )
    makrup.add(
        questionnaire_button
    ).add(
        form_start_button
    )
    return makrup

async def question_first_keyboard():
    makrup = InlineKeyboardMarkup()
    male_button = InlineKeyboardButton(
        "Male",
        callback_data="male_answer"
    )
    female_button = InlineKeyboardButton(
        "Female",
        callback_data="female_answer"
    )
    makrup.add(
        male_button
    ).add(
        female_button
    )
    return makrup







# async def city_question_keyboard():
#     makrup = InlineKeyboardMarkup()
#     bishkek_button = InlineKeyboardButton(
#         "Bishkek",
#         callback_data="bishkek_answer"
#     )
#     osh_button = InlineKeyboardButton(
#         "Osh",
#         callback_data="osh_answer"
#     )
#     cholpon_ata_button = InlineKeyboardButton(
#         "Cholpon Ata",
#         callback_data="cholpon_ata_answer"
#     )
#     naryn_button = InlineKeyboardButton(
#         "Naryn",
#         callback_data="naryn_answer"
#     )
#     talas_button = InlineKeyboardButton(
#         "Talas",
#         callback_data="talas_answer"
#     )
#     batken_button = InlineKeyboardButton(
#         "Batken",
#         callback_data="batken_answer"
#     )
#     jalal_abad_button = InlineKeyboardButton(
#         "Jalal Abad",
#         callback_data="jalal_abad_answer"
#     )
#     makrup.add(
#         bishkek_button
#     ).add(
#         osh_button
#     ).add(
#         cholpon_ata_button
#     ).add(
#         naryn_button
#     ).add(
#         batken_button
#     ).add(
#         talas_button
#     ).add(
#         jalal_abad_button
#     )

    # return makrup

async def my_profile_keyboard():
    markup = InlineKeyboardMarkup()
    profile_button = InlineKeyboardButton(
        "My Profile",
        callback_data="my_profile"
    )

    markup.add(
        profile_button
    )
    return markup