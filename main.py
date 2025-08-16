from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, InputMediaPhoto
from threading import Thread

import asyncio
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import parsing
import editTable
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
#BOT_TOKEN = "990455019:AAE8BUnr8d7gAGSAY1Ud4_UIVV6-qCThsns"
placeholder_photo = 'photos/main_frame.jpg'


start_keyboard = [
        [InlineKeyboardButton(str(parsing.voz("btn_hangout")[0]), callback_data="walking")],
        # [InlineKeyboardButton("Анкета", callback_data="quest")],
        [InlineKeyboardButton("О боте", callback_data="about")],
        [InlineKeyboardButton("Легкий квест", callback_data="light_quest")],
        [InlineKeyboardButton("Сложный квест", callback_data="hard_quest")],
        # [InlineKeyboardButton(str(parsing.voz("btn_rez")[0]), callback_data="residents")],
        # [InlineKeyboardButton("Главные события", callback_data='events')]
    ]

about_keyboard = [
        # [InlineKeyboardButton(str(parsing.voz("btn_about")[0]), callback_data="about")],
        [InlineKeyboardButton("Назад", callback_data="back")]
    ]

quest_keyboard = [
        [InlineKeyboardButton("Назад", callback_data="back")]
    ]

zone_keyboard = [
            # [InlineKeyboardButton(str(parsing.voz("btn_zonaMountain")[0]), callback_data="zone1")],
            # [InlineKeyboardButton(str(parsing.voz("btn_zoneWhater")[0]), callback_data="zone2")],
            # [InlineKeyboardButton(str(parsing.voz("btn_zoneSmallScene")[0]), callback_data="zone3")],
            # [InlineKeyboardButton(str(parsing.voz("btn_zoneBigScene")[0]), callback_data="zone4")],
            # [InlineKeyboardButton(str(parsing.voz("btn_zoneBigScene")[0]), callback_data="zone5")],
            [InlineKeyboardButton("Вокруг Соборной площади", callback_data="zone1")],
            [InlineKeyboardButton("Амбары и кузница", callback_data="zone2")],
            [InlineKeyboardButton("Мастерская и варница", callback_data="zone3")],
            [InlineKeyboardButton("Вокруг Покровской часовни-ротонды", callback_data="zone4")],
            [InlineKeyboardButton("Вокруг Соборной площади", callback_data="zone5")],
            [InlineKeyboardButton("Назад", callback_data="back")]
        ]
place1_keyboard = [
            [InlineKeyboardButton(str(parsing.voz("btn_spaso_preobrazhenskij_monastyr")[0]), callback_data="place11")],
            [InlineKeyboardButton(str(parsing.voz("btn_spaso_preobrazhenskij_sobor")[0]), callback_data="place12")],
            [InlineKeyboardButton(str(parsing.voz("btn_palaty_stroganovyh")[0]), callback_data="place13")],
            [InlineKeyboardButton(str(parsing.voz("btn_usadiba_golicyna")[0]), callback_data="place14")],
            [InlineKeyboardButton(str(parsing.voz("btn_incon_mother_of_good")[0]), callback_data="place15")],
            [InlineKeyboardButton(str(parsing.voz("btn_kolokolinya_s_torgovymi_ryadami")[0]), callback_data="place16")],
            [InlineKeyboardButton(str(parsing.voz("btn_dom_abamelek-lazareva")[0]), callback_data="place17")],
            [InlineKeyboardButton(str(parsing.voz("btn_dom_bragina")[0]), callback_data="place18")],
            #[InlineKeyboardButton("Задание 5", callback_data="quest5")],
            #[InlineKeyboardButton("Задание 4", callback_data="quest4")],
            [InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone")]
        ]
place2_keyboard = [
            [InlineKeyboardButton(str(parsing.voz("btn_ambar_pripasnoj_u_posada")[0]), callback_data="place21")],
            [InlineKeyboardButton(str(parsing.voz("btn_pripasnoj_ambar_u_lazarevyh")[0]), callback_data="place22")],
            [InlineKeyboardButton(str(parsing.voz("btn_ambar_golicynyh")[0]), callback_data="place23")],
            [InlineKeyboardButton(str(parsing.voz("btn_magazin_materialinyj")[0]), callback_data="place24")],
            [InlineKeyboardButton(str(parsing.voz("btn_kuznica_stroganovyh")[0]), callback_data="place25")],
            [InlineKeyboardButton(str(parsing.voz("btn_kuznica_golicynyh")[0]), callback_data="place26")],
            #[InlineKeyboardButton("Задание 3", callback_data="quest3")],
            #[InlineKeyboardButton("Задание 2", callback_data="quest2")],
            [InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone")]
        ]
place3_keyboard = [
            [InlineKeyboardButton(str(parsing.voz("btn_varnica_nikoliskaya")[0]), callback_data="place31")],
            [InlineKeyboardButton(str(parsing.voz("btn_mastreskaya_pri_promyslah_golicynyh")[0]), callback_data="place32")],
            #[InlineKeyboardButton("Задание 6", callback_data="quest6")],
            [InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone")]
        ]
place4_keyboard = [
            [InlineKeyboardButton(str(parsing.voz("btn_korpus_varochnyh_shuvalovyh")[0]), callback_data="place41")],
            [InlineKeyboardButton(str(parsing.voz("btn_korpus_parovoj_mashiny_shuvalovyh")[0]), callback_data="place42")],
            [InlineKeyboardButton(str(parsing.voz("btn_korpus_parovoj_mashiny_strogonovyh")[0]), callback_data="place43")],
            [InlineKeyboardButton(str(parsing.voz("btn_ambar_pripasnoj")[0]), callback_data="place44")],
            [InlineKeyboardButton(str(parsing.voz("btn_pokrovskaya_chasovnya_rotonda")[0]), callback_data="place45")],
            #[InlineKeyboardButton("Задание 7", callback_data="quest7")],
            [InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone")]
        ]
place5_keyboard = [
            [InlineKeyboardButton(str(parsing.voz("btn_Nikolskaya_tserkov")[0]), callback_data="place51")],
            [InlineKeyboardButton(str(parsing.voz("btn_yakoria_Usolia")[0]), callback_data="place52")],
            [InlineKeyboardButton(str(parsing.voz("btn_sirin")[0]), callback_data="place53")],
            [InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone")]
        ]




async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = start_keyboard
    await update.message.reply_photo(
        photo="photos/palaty stroganovykh.jpeg",
            )
    await update.message.reply_text(
        text=str(parsing.voz("btn_hello")[1]),
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "start" or query.data == "back":
        new_keyboard = start_keyboard
        with open(placeholder_photo, 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,
                caption="Главное меню"  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard))
        

    if query.data == "quest":
        new_keyboard = quest_keyboard
        with open(str(parsing.voz("btn_quest")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_quest")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )

    if query.data == "about" or query.data == "back_zone":
        new_keyboard = about_keyboard
        with open(str(parsing.voz("btn_about")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_about")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )

    if query.data == "light_quest" or query.data == "back_zone":
        new_keyboard = quest_keyboard
        with open(str(parsing.voz("btn_light_quest")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_light_quest")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )

    if query.data == "hard_quest" or query.data == "back_zone":
        new_keyboard = quest_keyboard
        with open(str(parsing.voz("btn_hard_quest")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_hard_quest")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )

    if query.data == "walking" or query.data == "back_zone":
        new_keyboard = zone_keyboard
        with open(placeholder_photo, 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,
                caption="Зоны"  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard))

    if query.data == "zone1" or query.data == "back_zone1":
        new_keyboard = place1_keyboard
        with open(placeholder_photo, 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,
                caption="Зона \"Двор вокруг Соборной площади\""  # Текст из вашего кода
        )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard))

    if query.data == "zone2" or query.data == "back_zone2":
        new_keyboard = place2_keyboard
        with open(placeholder_photo, 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,
                caption="Зона \"Амбары и кузницы\""  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard))
        
    if query.data == "zone3" or query.data == "back_zone3":
        new_keyboard = place3_keyboard
        with open(placeholder_photo, 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,
                caption="Зона \"Мастерская и варница\""  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard))
        
    if query.data == "zone4" or query.data == "back_zone4":
        new_keyboard = place4_keyboard
        with open(placeholder_photo, 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,
                caption="Зона \"Здания вокруг Покровской часовни-ротонды\""  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard))
        
    if query.data == "zone5" or query.data == "back_zone5":
        new_keyboard = place5_keyboard
        with open(placeholder_photo, 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,
                caption="Зона \"Здания вокруг Соборной площади\""  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard))

    if query.data == "place11":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone1")]]
        with open(str(parsing.voz("btn_spaso_preobrazhenskij_monastyr")[2][0]),'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_spaso_preobrazhenskij_monastyr")[1])  # Текст из вашего кода
        )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "place12":
        new_keyboard = [[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone1")]]
        with open(str(parsing.voz("btn_spaso_preobrazhenskij_sobor")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_spaso_preobrazhenskij_sobor")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "place13":
        new_keyboard = [[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone1")]]
        with open(str(parsing.voz("btn_palaty_stroganovyh")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_palaty_stroganovyh")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "place14":
        new_keyboard = [[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone1")]]
        with open(str(parsing.voz("btn_usadiba_golicyna")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_usadiba_golicyna")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "place15":
        new_keyboard = [[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone1")]]
        with open(str(parsing.voz("btn_incon_mother_of_good")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_incon_mother_of_good")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "place16":
        new_keyboard = [[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone1")]]
        with open(str(parsing.voz("btn_kolokolinya_s_torgovymi_ryadami")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_kolokolinya_s_torgovymi_ryadami")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "place17":
        new_keyboard = [[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone1")]]
        with open(str(parsing.voz("btn_dom_abamelek-lazareva")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_dom_abamelek-lazareva")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "place18":
        new_keyboard = [[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone1")]]
        with open(str(parsing.voz("btn_dom_bragina")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_dom_bragina")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )


    if query.data == "place21":
        new_keyboard = [[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone2")]]
        with open(str(parsing.voz("btn_ambar_pripasnoj_u_posada")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_ambar_pripasnoj_u_posada")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "place22":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone2")]]
        with open(str(parsing.voz("btn_pripasnoj_ambar_u_lazarevyh")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_pripasnoj_ambar_u_lazarevyh")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "place23":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone2")]]
        with open(str(parsing.voz("btn_ambar_golicynyh")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_ambar_golicynyh")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "place24":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone2")]]
        with open(str(parsing.voz("btn_magazin_materialinyj")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_magazin_materialinyj")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "place25":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone2")]]
        with open(str(parsing.voz("btn_kuznica_stroganovyh")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_kuznica_stroganovyh")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "place26":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone2")]]
        with open(str(parsing.voz("btn_kuznica_golicynyh")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_kuznica_golicynyh")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )

    if query.data == "place31":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone3")]]
        with open(str(parsing.voz("btn_varnica_nikoliskaya")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_varnica_nikoliskaya")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
        
    if query.data == "place32":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone3")]]
        with open(str(parsing.voz("btn_mastreskaya_pri_promyslah_golicynyh")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_mastreskaya_pri_promyslah_golicynyh")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )

    if query.data == "place41":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone4")]]
        with open(str(parsing.voz("btn_korpus_varochnyh_shuvalovyh")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_korpus_varochnyh_shuvalovyh")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "place42":
        new_keyboard = [[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone4")]]
        with open(str(parsing.voz("btn_korpus_parovoj_mashiny_shuvalovyh")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_korpus_parovoj_mashiny_shuvalovyh")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "place43":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone4")]]
        with open(str(parsing.voz("btn_korpus_parovoj_mashiny_strogonovyh")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_korpus_parovoj_mashiny_strogonovyh")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "place44":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone4")]]
        with open(str(parsing.voz("btn_ambar_pripasnoj")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_ambar_pripasnoj")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "place45":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone4")]]
        with open(str(parsing.voz("btn_pokrovskaya_chasovnya_rotonda")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_pokrovskaya_chasovnya_rotonda")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )

    if query.data == "place51":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone5")]]
        with open(str(parsing.voz("btn_Nikolskaya_tserkov")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_Nikolskaya_tserkov")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "place52":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone5")]]
        with open(str(parsing.voz("btn_yakoria_Usolia")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_yakoria_Usolia")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "place53":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone5")]]
        with open(str(parsing.voz("btn_sirin")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_sirin")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )






def getPhotoFile(url):
    return open


def bot_polling():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_button))
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(app.run_polling(stop_signals=None))

def main():
    Thread(target=bot_polling).start()
    editTable.start()

if __name__ == "__main__":
    main()

