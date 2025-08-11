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
placeholder_photo = 'photos/map.jpg'


start_keyboard = [
        [InlineKeyboardButton(str(parsing.voz("btn_hangout")[0]), callback_data="walking")],
        [InlineKeyboardButton("Программа выходного дня", url="https://blackweekend.yonote.ru/share/b2a7bec2-3738-4f95-bb62-d96f980d43bb")],
        [InlineKeyboardButton(str(parsing.voz("btn_rez")[0]), callback_data="residents")],
        [InlineKeyboardButton("Главные события", callback_data='events')]
    ]
residents_keyboard = [
        [InlineKeyboardButton(str(parsing.voz("btn_yrok")[0]), callback_data="rez1")],
        [InlineKeyboardButton(str(parsing.voz("btn_syvlav")[0]), callback_data="rez2")],
        [InlineKeyboardButton(str(parsing.voz("btn_myznal")[0]), callback_data="rez3")],
        [InlineKeyboardButton(str(parsing.voz("btn_gon")[0]), callback_data="rez4")],
        [InlineKeyboardButton(str(parsing.voz("btn_tkach")[0]), callback_data="rez5")],
        [InlineKeyboardButton(str(parsing.voz("btn_yralmerch")[0]), callback_data="rez6")],
        [InlineKeyboardButton(str(parsing.voz("btn_kyky")[0]), callback_data="rez7")],
        [InlineKeyboardButton(str(parsing.voz("btn_masttrav")[0]), callback_data="rez8")],
        [InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back")]
]
zone_keyboard = [
            [InlineKeyboardButton(str(parsing.voz("btn_zonaMountain")[0]), callback_data="zone1")],
            [InlineKeyboardButton(str(parsing.voz("btn_zoneWhater")[0]), callback_data="zone2")],
            [InlineKeyboardButton(str(parsing.voz("btn_zoneSmallScene")[0]), callback_data="zone3")],
            [InlineKeyboardButton(str(parsing.voz("btn_zoneBigScene")[0]), callback_data="zone4")],
            [InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back")]
        ]
place1_keyboard = [
            [InlineKeyboardButton(str(parsing.voz("btn_smotr")[0]), callback_data="place11")],
            [InlineKeyboardButton(str(parsing.voz("btn_artMore")[0]), callback_data="place12")],
            [InlineKeyboardButton(str(parsing.voz("btn_cherch")[0]), callback_data="place13")],
            [InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone")]
        ]
place2_keyboard = [
            [InlineKeyboardButton(str(parsing.voz("btn_artKapla")[0]), callback_data="place21")],
            [InlineKeyboardButton(str(parsing.voz("btn_artLodka")[0]), callback_data="place22")],
            [InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone")]
        ]
place3_keyboard = [
            [InlineKeyboardButton(str(parsing.voz("btn_skam")[0]), callback_data="place31")],
            [InlineKeyboardButton(str(parsing.voz("btn_gateway")[0]), callback_data="place32")],
            [InlineKeyboardButton(str(parsing.voz("btn_artShe")[0]), callback_data="place33")],
            [InlineKeyboardButton(str(parsing.voz("btn_artFromEarth")[0]), callback_data="place34")],
            [InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone")]
        ]
place4_keyboard = [
            [InlineKeyboardButton(str(parsing.voz("btn_stena")[0]), callback_data="place41")],
            [InlineKeyboardButton(str(parsing.voz("btn_cex")[0]), callback_data="place42")],
            [InlineKeyboardButton(str(parsing.voz("btn_artDomiki")[0]), callback_data="place43")],
            [InlineKeyboardButton(str(parsing.voz("btn_nal")[0]), callback_data="place44")],
            [InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone")]
        ]
events_keyboard=[
            [InlineKeyboardButton("Масленица", url="https://vk.com/club204815708")],
            [InlineKeyboardButton("Демидов Фест", url="https://vk.com/club214641997")],
            [InlineKeyboardButton("Заговельнички", url="https://vk.com/club215953798")],
            [InlineKeyboardButton("Веселые холмы", url="https://vk.com/funnyhills")],
            [InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back")]
        ]




async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton(str(parsing.voz("btn_start")[0]), callback_data="start")]]
    await update.message.reply_photo(
        photo=str(parsing.voz("btn_zavod")[2][0]),
            )
    await update.message.reply_text(
        text=str(parsing.voz("btn_zavod")[1])
    )
    await update.message.reply_photo(
        photo=str(parsing.voz("btn_vesh")[2][0])
    )
    await update.message.reply_text(
        text=str(parsing.voz("btn_vesh")[1])
    )
    await update.message.reply_photo(
        photo=str(parsing.voz("btn_nav")[2][0])
    )
    await update.message.reply_text(
        text=str(parsing.voz("btn_nav")[1]),
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
                caption="Зона \"Гора\""  # Текст из вашего кода
        )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard))

    if query.data == "zone2" or query.data == "back_zone2":
        new_keyboard = place2_keyboard
        with open(placeholder_photo, 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,
                caption="Зона \"Вода\""  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard))
    if query.data == "zone3" or query.data == "back_zone3":
        new_keyboard = place3_keyboard
        with open(placeholder_photo, 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,
                caption="Зона \"Малая сцена\""  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard))
    if query.data == "zone4" or query.data == "back_zone4":
        new_keyboard = place4_keyboard
        with open(placeholder_photo, 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,
                caption="Зона \"Большая сцена\""  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard))


    if query.data == "residents" or query.data == "back_rez":
        new_keyboard = residents_keyboard
        with open(placeholder_photo, 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_rez")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )

    if query.data == "events":
        new_keyboard = events_keyboard
        with open(placeholder_photo, 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption="Главные события года"  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )

    if query.data == "place11":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone1")]]
        with open(str(parsing.voz("btn_smotr")[2][0]),'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_smotr")[1])  # Текст из вашего кода
        )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "place12":
        new_keyboard = [[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone1")]]
        with open(str(parsing.voz("btn_artMore")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_artMore")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "place13":
        new_keyboard = [[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone1")]]
        with open(str(parsing.voz("btn_cherch")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_cherch")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "place21":
        new_keyboard = [[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone2")]]
        with open(str(parsing.voz("btn_artKapla")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_artKapla")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "place22":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone2")]]
        with open(str(parsing.voz("btn_artLodka")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_artLodka")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )

    if query.data == "place31":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone3")]]
        with open(str(parsing.voz("btn_skam")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_skam")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "place32":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone3")]]
        with open(str(parsing.voz("btn_gateway")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_gateway")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "place33":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone3")]]
        with open(str(parsing.voz("btn_artShe")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_artShe")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "place34":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone3")]]
        with open(str(parsing.voz("btn_artFromEarth")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_artFromEarth")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "place41":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone4")]]
        with open(str(parsing.voz("btn_stena")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_stena")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "place42":
        new_keyboard = [[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone4")]]
        with open(str(parsing.voz("btn_cex")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_cex")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "place43":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone4")]]
        with open(str(parsing.voz("btn_artDomiki")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_artDomiki")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "place44":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone4")]]
        with open(str(parsing.voz("btn_nal")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_nal")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )

    if query.data == "rez1":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_rez")]]
        with open(str(parsing.voz("btn_yrok")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_yrok")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "rez2":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_rez")]]
        with open(str(parsing.voz("btn_syvlav")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_syvlav")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "rez3":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_rez")]]
        with open(str(parsing.voz("btn_myznal")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_myznal")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "rez4":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_rez")]]
        with open(str(parsing.voz("btn_gon")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_gon")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "rez5":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_rez")]]
        with open(str(parsing.voz("btn_tkach")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_tkach")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "rez6":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_rez")]]
        with open(str(parsing.voz("btn_yralmerch")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_yralmerch")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "rez7":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_rez")]]
        with open(str(parsing.voz("btn_kyky")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_kyky")[1])  # Текст из вашего кода
            )
        await query.edit_message_media(
            media=media,
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "rez8":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_rez")]]
        with open(str(parsing.voz("btn_masttrav")[2][0]), 'rb') as photo_file:
            media = InputMediaPhoto(
                media=photo_file,  # URL изображения или file_id
                caption=str(parsing.voz("btn_masttrav")[1])  # Текст из вашего кода
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

